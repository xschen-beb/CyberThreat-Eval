from threat_research import threat_research_playground
import os
from test_cassie_triage import get_recent_urls
from concurrent.futures import ThreadPoolExecutor, as_completed
from add_work_item_comments import add_comment_to_workitem
import logging

# Setup logging
logging.basicConfig(
    filename="processing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

f_eval = open("example.md", "w")

links = [
# 'https://www.cyfirma.com/research/hexon-stealer-the-long-journey-of-copying-hiding-and-rebranding',
# "https://www.bleepingcomputer.com/news/security/bumblebee-malware-returns-after-recent-law-enforcement-disruption/",
# "https://www.cyfirma.com/research/the-will-of-d-a-deep-dive-into-divulge-stealer-dedsec-stealer-and-duck-stealer/",
# "https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/fake-attachment-roundcube-mail-server-attacks-exploit-cve-2024-37383-vulnerability",
# "https://www.cybereason.com/blog/threat-analysis-beast-ransomware",
#"https://www.elastic.co/security-labs/tricks-and-treats"
#"https://www.bleepingcomputer.com/news/security/qubitstrike-attacks-rootkit-jupyter-linux-servers-to-steal-credentials/"
# "https://www.bleepingcomputer.com/news/security/us-treasury-department-breached-through-remote-support-platform/",
# "https://www.bankinfosecurity.com/four-faith-routers-exploited-using-new-flaw-a-27179",
# "https://www.bankinfosecurity.com/hackers-launch-supply-chain-attack-against-chrome-extensions-a-27173",
# "https://www.bleepingcomputer.com/news/security/hackers-exploit-four-faith-router-flaw-to-open-reverse-shells/",
# "https://www.fortinet.com/blog/threat-research/catching-ec2-grouper-no-indicators-required",
# "https://www.fortinet.com/blog/threat-research/botnets-continue-to-target-aging-d-link-vulnerabilities#new_tab",
# "https://www.bleepingcomputer.com/news/microsoft/microsoft-issues-urgent-dev-warning-to-update-net-installer-link/",
# "https://blog.checkpoint.com/securing-user-and-access/the-email-security-revolution-how-the-market-landscape-has-changed/",
# "https://www.dragos.com/blog/top-5-cybersecurity-threats-to-oil-gas-and-how-to-protect-against-them/",
# "https://isc.sans.edu/diary/rss/31550",
# "https://www.bleepingcomputer.com/news/security/atandt-and-verizon-say-networks-secure-after-salt-typhoon-breach/"
# "https://blog.checkpoint.com/customer-stories/fast-pace-health-zero-phishing-incidents-since-harmony-email-collaboration-implementation/",
# "https://www.darkreading.com/endpoint-security/trend-micro-and-intel-innovate-to-weed-out-covert-threats",
# "https://www.bleepingcomputer.com/news/security/unpatched-critical-flaws-impact-fancy-product-designer-wordpress-plugin/",
# "https://socradar.io/black-basta-deploying-zbot-darkgate-bespoke-malware/",
# "https://www.bleepingcomputer.com/news/security/ivanti-warns-of-new-connect-secure-flaw-used-in-zero-day-attacks/",
# "https://www.bleepingcomputer.com/news/security/russian-isp-confirms-ukrainian-hackers-destroyed-its-network/",
# "https://www.bleepingcomputer.com/news/security/sonicwall-urges-admins-to-patch-exploitable-sslvpn-bug-immediately/"
# the followings are 250113
# "https://gbhackers.com/eagerbee-malware/",
# "https://www.googlecloudcommunity.com/gc/Community-Blog/Finding-Malware-Unveiling-PLAYFULGHOST-with-Google-Security/ba-p/850676#new_tab",
# "https://socradar.io/cerberus-multi-stage-trojan-banking-campaign/"
# "https://www.malwarebytes.com/blog/news/2025/01/can-you-try-a-game-i-made-fake-game-sites-lead-to-information-stealers",
# "https://socradar.io/dark-web-profile-kairos-extortion-group/"
# "https://gbhackers.com/north-korean-hackers-wipe-cryptocurrency-wallets-via-fake-job-interviews/",
# "https://trac-labs.com/advancing-through-the-cyberfront-legionloader-commander-6af38ebe39d4",
# "https://www.bankinfosecurity.com/36-chrome-extensions-compromised-in-supply-chain-attack-a-27207",
# "https://socket.dev/blog/quasar-rat-disguised-as-an-npm-package#new_tab"
# 250114
# "https://gbhackers.com/ot-products-security-guide/",
# "https://www.bleepingcomputer.com/news/security/ransomware-abuses-amazon-aws-feature-to-encrypt-s3-buckets/",
# "https://research.checkpoint.com/2025/banshee-macos-stealer-that-stole-code-from-macos-xprotect"
]
"https://www.bleepingcomputer.com/news/security/hackers-exploit-keriocontrol-firewall-flaw-to-steal-admin-csrf-tokens/"
# "https://www.malwarebytes.com/blog/news/2023/01/preinstalled-malware-infested-t95-tv-box-from-amazon"
# "https://blog.checkpoint.com/customer-stories/fast-pace-health-zero-phishing-incidents-since-harmony-email-collaboration-implementation/"
# 250115
# links = ['https://www.bleepingcomputer.com/news/microsoft/january-windows-updates-may-fail-if-citrix-sra-is-installed/', 'https://www.bleepingcomputer.com/news/legal/allstate-car-insurer-sued-for-tracking-drivers-without-permission/', 'https://www.bleepingcomputer.com/news/security/wp3xyz-malware-attacks-add-rogue-admins-to-5-000-plus-wordpress-sites/', 'https://www.bleepingcomputer.com/news/security/us-govt-says-north-korea-stole-over-659-million-in-crypto-last-year/', 'https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/cve-2024-55591-fortinet-fortios-fortiproxy-zero-day/', 'https://www.bankinfosecurity.com/fbi-deletes-more-than-4000-plugx-malware-instances-a-27285', 'https://www.bleepingcomputer.com/news/security/google-oauth-flaw-lets-attackers-gain-access-to-abandoned-accounts/', 'https://www.bleepingcomputer.com/news/security/hackers-use-fasthttp-in-new-high-speed-microsoft-365-password-attacks/', 'https://blogs.infoblox.com/threat-intelligence/one-mikro-typo-how-a-simple-dns-misconfiguration-enables-malware-delivery-by-a-russian-botnet/', 'https://www.bleepingcomputer.com/news/security/fortinet-warns-of-auth-bypass-zero-day-exploited-to-hijack-firewalls/', 'https://asec.ahnlab.com/en/85758/', 'https://unit42.paloaltonetworks.com/graph-neural-networks/']
# links = ["https://www.bleepingcomputer.com/news/security/ransomware-abuses-amazon-aws-feature-to-encrypt-s3-buckets/",]
# 250116
# links = ['https://www.bleepingcomputer.com/news/security/label-giant-avery-says-website-hacked-to-steal-credit-cards/', 'https://www.bleepingcomputer.com/news/security/over-660-000-rsync-servers-exposed-to-code-execution-attacks/', 'https://www.wiz.io/blog/wiz-research-identifies-exploitation-in-the-wild-of-aviatrix-cve-2024-50603', 'https://blog.talosintelligence.com/slew-of-wavlink-vulnerabilities/']
"""
# links_dict = {
    '18447575': 'https://intezer.com/blog/malware-analysis/weaponized-software-targets-chinese/', '18446105': 'https://www.bleepingcomputer.com/news/security/gdpr-complaints-filed-against-tiktok-temu-for-sending-user-data-to-china/', '18445871': 'https://www.guidepointsecurity.com/blog/ransomhub-affiliate-leverage-python-based-backdoor/#new_tab', '18445870': 'https://www.welivesecurity.com/en/eset-research/under-cloak-uefi-secure-boot-introducing-cve-2024-7344/#new_tab', '18445859': 'https://www.bleepingcomputer.com/news/security/w3-total-cache-plugin-flaw-exposes-1-million-wordpress-sites-to-attacks/', '18445858': 'https://www.bleepingcomputer.com/news/security/microsoft-expands-testing-of-windows-11-admin-protection-feature/', '18445848': 'https://blog.talosintelligence.com/find-the-helpers/', '18445841': 'https://www.bleepingcomputer.com/news/security/us-cracks-down-on-north-korean-it-worker-army-with-more-sanctions/', '18445842': 'https://www.bleepingcomputer.com/news/security/biden-signs-executive-order-to-bolster-national-cybersecurity/', '18445819': 'https://blog.sekoia.io/sneaky-2fa-exposing-a-new-aitm-phishing-as-a-service/', '18445827': 'https://news.sophos.com/en-us/2025/01/16/gootloader-inside-out/', '18445820': 'https://www.bleepingcomputer.com/news/security/wolf-haldenstein-law-firm-says-35-million-impacted-by-data-breach/', '18445821': 'https://www.bleepingcomputer.com/news/security/ftc-sues-godaddy-for-years-of-poor-hosting-security-practices/', '18445822': 'https://www.bleepingcomputer.com/news/security/new-uefi-secure-boot-flaw-exposes-systems-to-bootkits-patch-now/', '18445823': 'https://www.bleepingcomputer.com/news/security/mfa-failures-the-worst-is-yet-to-come/', '18445791': 'https://cyble.com/blog/ukraine-cyberthreat-landscape-2024/', '18445792': 'https://cyble.com/blog/hitachi-energy-critical-risk/', '18445860': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-06', '18445861': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-01', '18445862': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-05', '18445863': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-04', '18445864': 'https://www.cisa.gov/news-events/ics-advisories/icsa-25-016-07'
}
"""
# links = ['https://www.bleepingcomputer.com/news/microsoft/microsoft-ends-support-for-office-apps-on-windows-10-in-october/']
# 250117
"""
links_dict = {
    '18448284': 'https://www.bleepingcomputer.com/news/security/malicious-pypi-package-steals-discord-auth-tokens-from-devs/',
    '18448272': 'https://www.acronis.com/en-us/cyber-protection-center/posts/tmpn-skuld-stealer-the-dark-side-of-open-source/',
    '18448268': 'https://www.cyfirma.com/research/android-malware-in-donot-apt-operations/',
    '18448262': 'https://www.bleepingcomputer.com/news/security/us-sanctions-chinese-firm-hacker-behind-telecom-and-treasury-hacks/',
    '18448258': 'https://www.esentire.com/blog/mintsloader-stealc-and-boinc-delivery',
    '18448132': 'https://cyble.com/blog/sliver-implant-targets-german-entities-with-dll-sideloading-and-proxying-techniques/',
    '18448244': 'https://cert.gov.ua/article/6282069'
}
"""
url = {'12i909': 'https://socradar.io/black-basta-deploying-zbot-darkgate-bespoke-malware'}

def pipeline_ver0(output_dir):
    links_dict = get_recent_urls()
    # print(links_dict)
    # links_dict = {'2312we3': 'https://www.wiz.io/blog/wiz-research-identifies-exploitation-in-the-wild-of-aviatrix-cve-2024-50603'}
    # links_dict = {
        # '12i909': 'https://socradar.io/black-basta-deploying-zbot-darkgate-bespoke-malware',
        # '323wd': 'https://www.bleepingcomputer.com/news/security/russian-isp-confirms-ukrainian-hackers-destroyed-its-network'
        # '323wd': 'https://www.bleepingcomputer.com/news/security/mikrotik-botnet-uses-misconfigured-spf-dns-records-to-spread-malware'
        # '323wd': 'https://www.bleepingcomputer.com/news/security/ivanti-warns-of-new-connect-secure-flaw-used-in-zero-day-attacks'
    # }

    output_location = output_dir
    failed_links = []
    saved_paths = {}  # Dictionary to store {work_id: file_path}

    if not os.path.exists(output_location):
        os.makedirs(output_location)

    for work_id, link in list(links_dict.items())[:10]:
        # Normalize the link to remove trailing slashes
        if link.endswith("/"):
            link = link[:-1]

        # Generate the file name
        file_name = os.path.join(output_location, link.split("/")[-1] + ".md")

        # Check if the file already exists
        if os.path.exists(file_name):
            print(f"File already exists for link: {link}. Skipping...")
            saved_paths[work_id] = file_name  # Add existing file to dictionary
            continue

        try:
            # Generate content for the link
            text_output = threat_research_playground(link, work_id)
            print(f"Output for link {link}: \n{text_output}")

            # Write the content to the file
            with open(file_name, "w", encoding="utf-8") as fw:
                fw.write(text_output)
                print(f"Successfully wrote to {file_name}")

            # Add the successfully processed file to the dictionary
            saved_paths[work_id] = file_name

        except Exception as e:
            # Log the failed link and continue with the next one
            print(f"Error processing {link}: {e}")
            failed_links.append({"work_id": work_id, "link": link, "error": str(e)})

    # Print all failed links at the end
    if failed_links:
        print("\nFailed to process the following links:")
        for failed_link in failed_links:
            print(f"- Work ID: {failed_link['work_id']}, Link: {failed_link['link']}, Error: {failed_link['error']}")

    # Return the dictionary containing {work_id: file_path}
    print(f"Saved paths: {saved_paths}")
    return saved_paths

def process_link(work_id, link, output_location):
    """Process a single link and save its content."""
    try:
        # Normalize the link to remove trailing slashes
        if link.endswith("/"):
            link = link[:-1]

        # Generate the file name
        file_name = os.path.join(output_location, link.split("/")[-1] + ".md")

        # Check if the file already exists
        if os.path.exists(file_name):
            logging.info(f"File already exists for link: {link}. Skipping...")
            return None

        # Generate content for the link
        text_output = threat_research_playground(link, work_id)

        # Write the content to the file
        with open(file_name, "w", encoding="utf-8") as fw:
            fw.write(text_output)
            logging.info(f"Successfully wrote to {file_name}")
        return None

    except Exception as e:
        logging.error(f"Error processing link {link}: {e}")
        return {"work_id": work_id, "link": link, "error": str(e)}  # Return details of the failure

def main():
    links_dict = get_recent_urls()
    print(links_dict)
    output_location = "250123/"
    if not os.path.exists(output_location):
        os.makedirs(output_location)

    failed_links = []
    max_workers = 3  # Adjust the number of workers based on system resources

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_link = {
            executor.submit(process_link, work_id, link, output_location): link
            for work_id, link in links_dict.items()
        }

        for future in as_completed(future_to_link):
            result = future.result()
            if result:  # If the result contains error details, add to failed_links
                failed_links.append(result)

    # Print and log all failed links at the end
    if failed_links:
        logging.warning("Failed to process the following links:")
        for failure in failed_links:
            logging.warning(f"- Work ID: {failure['work_id']}, Link: {failure['link']}, Error: {failure['error']}")
    else:
        logging.info("All links processed successfully.")

if __name__ == '__main__':
    output_dir = "250124"
    # save_links = pipeline_ver0(output_dir)
    # item_id = '18456546'
    # file_id = '250124\\31600.md'

    item_id = '18456152'
    file_id = '250124\\fbi-north-korean-it-workers-steal-source-code-to-extort-employers.md'
    fo = open(file_id, 'r', encoding='utf-8')
    markdown = fo.read()
    print(markdown)
    response = add_comment_to_workitem(item_id, markdown)
    print(response)