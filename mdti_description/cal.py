

if __name__ == '__main__':
    data = [
        {"file": "AgentGenReport\\1106\\north-korean-hackers-use-new-macos-malware-against-crypto-firms.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1106\\the-evolution-of-transparent-tribes-new-malware.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 5, "Comprehensiveness": 5, "Clarity": 5, "Coherence": 5, "Attribution": 5}},
        {"file": "AgentGenReport\\1106\\veildrive-microsoft-services-malware-c2#new_tab.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1111\\amazon-confirms-employee-data-breach-after-vendor-hack.md", "evaluation_scores": {"Relevance": 3, "Accuracy": 3, "Comprehensiveness": 3, "Clarity": 4, "Coherence": 4, "Attribution": 2}},
        {"file": "AgentGenReport\\1112\\hamas-linked-threat-group-expands-espionage-and-destructive-operations.md", "evaluation_scores": {"Relevance": 4, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 3}},
        {"file": "AgentGenReport\\1112\\north-korean-hackers-create-flutter-apps-to-bypass-macos-security.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1112\\volt-typhoon-rebuilds-malware-botnet-following-fbi-disruption.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 4, "Comprehensiveness": 5, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1114\\chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach.md", "evaluation_scores": {"Relevance": 1, "Accuracy": 1, "Comprehensiveness": 1, "Clarity": 4, "Coherence": 4, "Attribution": 1}},
        {"file": "AgentGenReport\\1114\\Zero-day-cve-2024-4351-report.pdf.md", "evaluation_scores": {"Relevance": 3, "Accuracy": 4, "Comprehensiveness": 3, "Clarity": 5, "Coherence": 5, "Attribution": 3}},
        {"file": "AgentGenReport\\1115\\84531.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1115\\brazenbamboo-weaponizes-forticlient-vulnerability-to-steal-vpn-credentials-via-deepdata.md", "evaluation_scores": {"Relevance": 4, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 3}},
        {"file": "AgentGenReport\\1118\\inside-intelligence-center-financially-motivated-chinese-threat-actor-silkspecter-targeting-black-friday-shoppers#a3#new_tab.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1118\\lightspy-apt41-deploys-advanced-deepdata-framework-in-targeted-southern-asia-espionage-campaign#new_tab.md", "evaluation_scores": {"Relevance": 3, "Accuracy": 3, "Comprehensiveness": 3, "Clarity": 4, "Coherence": 4, "Attribution": 2}},
        {"file": "AgentGenReport\\1118\\security-brief-clickfix-social-engineering-technique-floods-threat-landscape.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 3}},
        {"file": "AgentGenReport\\1119\\chinese-hackers-exploit-fortinet-vpn-zero-day-to-steal-credentials1.md", "evaluation_scores": {"Relevance": 4, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1119\\critical-rce-bug-in-vmware-vcenter-server-now-exploited-in-attacks1.md", "evaluation_scores": {"Relevance": 4, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 3}},
        {"file": "AgentGenReport\\1119\\lodeinfo-campaign-of-earth-kasha.html1.md", "evaluation_scores": {"Relevance": 4, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1119\\ngioweb-botnet-fueling-residential-proxies-disrupted-in-cybercrime-crackdown1.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 5, "Comprehensiveness": 5, "Clarity": 5, "Coherence": 5, "Attribution": 5}},
        {"file": "AgentGenReport\\1120\\sophos-mdr-blocks-and-tracks-activity-from-probable-iranian-state-actor-muddywater.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 5, "Comprehensiveness": 5, "Clarity": 5, "Coherence": 5, "Attribution": 5}},
        {"file": "AgentGenReport\\1121\\dprk-it-workers-a-network-of-active-front-companies-and-their-links-to-china.md", "evaluation_scores": {"Relevance": 4, "Accuracy": 3, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 3}},
        {"file": "AgentGenReport\\1122\\bidirectional-communication-via-polyrhythms-and-shuffles-without-jon-the-beat-must-go-on.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 3}},
        {"file": "AgentGenReport\\1122\\the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access.md", "evaluation_scores": {"Relevance": 5, "Accuracy": 5, "Comprehensiveness": 5, "Clarity": 5, "Coherence": 5, "Attribution": 5}},
        {"file": "AgentGenReport\\1125\\#new_tab.md", "known": "known", "source": "malpedia", "evaluation_scores": {"Relevance": 5, "Accuracy": 5, "Comprehensiveness": 5, "Clarity": 5, "Coherence": 5, "Attribution": 5}},
        {"file": "AgentGenReport\\1125\\firefox-and-windows-zero-days-exploited-by-russian-romcom-hackers.md", "known": "known", "source": "malpedia", "evaluation_scores": {"Relevance": 5, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1126-27\\rockstar-2fa-a-driving-force-in-phishing-as-a-service-paas.md", "known": "known", "source": "malpedia", "evaluation_scores": {"Relevance": 4, "Accuracy": 4, "Comprehensiveness": 4, "Clarity": 5, "Coherence": 5, "Attribution": 4}},
        {"file": "AgentGenReport\\1126-27\\the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access.md", "known": "known", "source": "malpedia", "evaluation_scores": {"Relevance": 5, "Accuracy": 5, "Comprehensiveness": 5, "Clarity": 5, "Coherence": 5, "Attribution": 5}},
    ]
    sums = {"Relevance": 0, "Accuracy": 0, "Comprehensiveness": 0, "Clarity": 0, "Coherence": 0, "Attribution": 0}
    num_entries = len(data)

    # Sum the scores
    for entry in data:
        scores = entry["evaluation_scores"]
        for key in sums:
            sums[key] += scores[key]

    # Calculate averages
    averages = {key: sums[key] / num_entries for key in sums}

    print(averages)