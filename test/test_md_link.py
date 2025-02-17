import re

def convert_star_links_to_markdown(text):
    pattern = re.compile(r"\*([^*]+)\*\s?\((https?://[^\s)]+)\)")

    def replace_func(match):
        link_text = match.group(1).strip()
        link_url  = match.group(2)

        return f"[*{link_text}*]({link_url})"

    new_text = pattern.sub(replace_func, text)
    return new_text


def process_text(text):
    pattern_your_changes = re.compile(
        r"\*Your\s+changes\*\s?\((https?://[^\s)]+)\)",
        flags=re.IGNORECASE
    )
    text_step1 = pattern_your_changes.sub(lambda m: f"({m.group(1)})", text)

    pattern_consecutive_links = re.compile(
        r"\)\.\s?\("
        r"(https?://[^\s)]+)\)"
    )

    def merge_links(match):
        return f")({match.group(1)})"

    text_step2 = text_step1
    while True:
        new_text = pattern_consecutive_links.sub(merge_links, text_step2)
        if new_text == text_step2:
            break
        text_step2 = new_text


    pattern_sentence_link = re.compile(
        r"([^.\n]+)\.\s*\(("
        r"(?:https?://[^\s)]+)\)"
        r"(?:\(https?://[^\s)]+\))*"  #
        r")"
    )

    def sentence_to_markdown(match):
        sentence_text = match.group(1).strip()
        link_part = match.group(2) 
        return f"[{sentence_text}.]{link_part}"

    text_step3 = pattern_sentence_link.sub(sentence_to_markdown, text_step2)

    return text_step3


if __name__ == "__main__":
    # input_text = """#### Root cause \n The root cause of the incident was the exploitation of two zero-day vulnerabilities (CVE-2024-12356 and CVE-2024-12686) in BeyondTrust's Remote Support SaaS platform. The threat actors utilized a stolen Remote Support SaaS API key to reset passwords for local application accounts and gain further privileged access to the systems. *BeyondTrust cybersecurity company detected the breach on December 2nd, 2024, and conducted a root cause analysis on December 5th, 2024* (https://www.bleepingcomputer.com/news/security/beyondtrust-says-hackers-breached-remote-support-saas-instances/). *Security Advisory BT24-10 and BT24-11 were issued to address the vulnerabilities* (https://blog.gitguardian.com/what-happened-in-the-u-s-department-of-the-treasury-breach-a-detailed-summary/). *CISA is working closely with the Treasury Department and BeyondTrust to understand and mitigate the impacts* (https://www.cisa.gov/news-events/news/cisa-update-treasury-breach). *The vulnerabilities included a Command Injection Vulnerability (CVE-2024-12356) and a Post-Exploitation Privilege Escalation (CVE-2024-12686)* (https://socradar.io/beyondtrust-security-incident-command-injection/). *BeyondTrust's 20,000 customers across 100 countries were notified* (https://www.darkreading.com/cyberattacks-data-breaches/chinese-state-hackers-breach-us-treasury-department). *The API key was obtained from BeyondTrust, a third-party vendor* (https://www.cpomagazine.com/cyber-security/us-treasury-breached-by-chinese-state-sponsored-hackers-via-stolen-api-key/)."""
    # input_text = """
# The attack potentially impacted all users of the compromised Chrome extensions, with specific mention of targeting Facebook Ads accounts and stealing Facebook access tokens, user passwords, and session tokens. The malicious code added a mouse click listener for Facebook.com to retrieve images, presumably searching for QR codes to bypass captchas and/or 2FA authorization requests *Your changes* (https://www.securityweek.com/several-chrome-extensions-compromised-in-supply-chain-attack/). *Your changes* (https://www.darkreading.com/application-security/chrome-extension-compromises-highlight-software-supply-challenges). The attack affected 2.6 million people. *Your changes* (https://socradar.io/phishing-attack-cyberhaven-chrome-extension/). The retail and hospitality sectors face significant risks, including data breaches and compliance violations *Your changes* (https://rhisac.org/threat-intelligence/cyberhaven-extension-compromise-part-of-broader-campaign-affecting-multiple-chrome-extensions/). 
# """
    # output_text = process_text(input_text)
    # print(output_text)
    pass