import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.threat_research import *

def test(url, ttp_text):
    text_output = ""
    source_blog = click_into_page_with_browser(url)

    actors = get_actor_v1(source_blog)
    threat_actors = eval(actors)
    print("==> Extracted threat actors from the report: ", actors)

    has_mitigation = False
    mitigation_content = ""

    # Step 1: Extract from MDTI
    if actors and 'None' not in actors:
        names, links, mdti_recommendation = mdti_recommendation_pipeline(threat_actors, token)
        print("==> Extracted mitigation from MDTI: ", names, links, mdti_recommendation)

        if mdti_recommendation:  # If MDTI found recommendations
            valid_links = []
            for link in links:
                try:
                    blog_content = click_into_page_with_browser(link)
                    num_tokens = num_tokens_from_string(blog_content, "gpt-4o")
                    if num_tokens > 500:
                        valid_links.append(link)
                except Exception as e:
                    print(f"Error processing {link}: {e}")

            for i in range(len(mdti_recommendation)):
                mitigation_content += f"- Based on MDTI profile for ({names[i]}) from the following links:\n\n{links[i]}\n\nThe recommendations are:\n\n{mdti_recommendation[i]}\n"
            
            has_mitigation = True

    # Step 2: If MDTI fails, use OSINT Recommendation Dictionary
    if not has_mitigation:
        rec_dict_mitigation = gen_dict_recommendation_from_report(source_blog)
        if rec_dict_mitigation:
            print(f"==> Extracted mitigation category from the report: {rec_dict_mitigation}")
            tech = pd.read_csv('recommendations/RecDict.csv')
            res = get_recommendation_by_title(tech, rec_dict_mitigation)
            mitigation_content += f"- Based on OSINT recommendation dictionary ({rec_dict_mitigation}), the recommendations are:\n\n{rec_dict_mitigation}: {res[1]}\n"
            has_mitigation = True

    # Step 3: If OSINT fails, use TTP-based recommendations
    if not has_mitigation:
        mitigation = process_all_ttps(ttp_text)
        if mitigation:
            print("==> Using TTP-based recommendations as fallback.")
            mitigation_content += "- Based on TTPs, we suggest the following recommendations:\n"
            for rec in mitigation:
                mitigation_content += f"- [{rec['ttp_id']}] {rec['title']}: {rec['reason']}\n"
            has_mitigation = True

    # Step 4: If everything fails, add default message
    if not has_mitigation:
        print("==> No recommendations found in MDTI, OSINT, or TTPs.")
        mitigation_content = "- No specific mitigation steps were found.\n"

    # Append final content to output
    text_output += mitigation_content + "\n"

    print(f"After mitigation, \n\n{text_output}\n\n")

if __name__ == '__main__':
    url = 'https://www.trendmicro.com/en_us/research/25/a/cve-2025-0411-ukrainian-organizations-targeted.html'

    ttp_text = """
    - T1566.001: Phishing: Spearphishing Attachment;
  Confidence: High.
  Justification: The report mentions spear-phishing campaigns using homoglyph attacks to spoof document extensions and trick users into executing malicious files.
- T1203: Exploitation for Client Execution;
  Confidence: High.
  Justification: The exploitation of the 7-Zip zero-day vulnerability (CVE-2025-0411) to bypass MoTW protections and execute malicious content.
- T1071.001: Application Layer Protocol: Web Protocols;
  Confidence: Medium.
  Justification: The use of URLs in phishing emails to point to attacker-controlled servers hosting additional malicious files.
- T1059.007: Command and Scripting Interpreter: JavaScript;
  Confidence: Medium.
  Justification: The execution of JavaScript files as part of the attack chain once the MoTW protections are bypassed.
    """
    test(url, ttp_text)