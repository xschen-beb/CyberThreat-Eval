from threat_research import threat_research_playground

f_eval = open("demo.txt", "w")

links = [
"https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/",
# "https://www.bleepingcomputer.com/news/security/bumblebee-malware-returns-after-recent-law-enforcement-disruption/",
# "https://www.cyfirma.com/research/the-will-of-d-a-deep-dive-into-divulge-stealer-dedsec-stealer-and-duck-stealer/",
# "https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/fake-attachment-roundcube-mail-server-attacks-exploit-cve-2024-37383-vulnerability",
# "https://www.cybereason.com/blog/threat-analysis-beast-ransomware",
#"https://www.elastic.co/security-labs/tricks-and-treats"
]
# "https://www.malwarebytes.com/blog/news/2023/01/preinstalled-malware-infested-t95-tv-box-from-amazon"
num = 0
for link in links:
    num += 1
    f_eval.write(str(num) + "============================================" + "\n")
    text_output = threat_research_playground(link)
    # a = threat_research_playground("https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a")
    print(text_output)
    f_eval.write(text_output)