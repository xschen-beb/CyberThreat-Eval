# Keys are the subject matter categories, values are the targeting categories and their corresponding scores
# Example:
# Subject Matter: Defacement / Spam, Targeting: ICS, Priority Score: 1

priority_mapping = {
    "Defacement / Spam": {
        "Unknown/NA": 5, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 3, "Industry/Sector": 3,
        "Platform/Service": 3, "Drive-by": 3, "ICS": 1
    },
    "Mobile Malware": {
        "Unknown/NA": 3, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 3, "Industry/Sector": 3,
        "Platform/Service": 3, "Drive-by": 3, "ICS": 5
    },
    "Malware Updates": {
        "Unknown/NA": 2, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 2, "Industry/Sector": 2,
        "Platform/Service": 2, "Drive-by": 2, "ICS": 1
    },
    "New Malware": {
        "Unknown/NA": 3, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 2, "Industry/Sector": 2,
        "Platform/Service": 2, "Drive-by": 2, "ICS": 1
    },
    "Vulnerability Exploitation (CVE < 9)": {
        "Unknown/NA": 5, "Singular System": 2, "Singular Company": 2,
        "Singular Country": 5, "Multiple Countries": 5, "Industry/Sector": 5,
        "Platform/Service": 2, "Drive-by": 5, "ICS": 1
    },
    "Cryptominer / Resource Hijacking": {
        "Unknown/NA": 3, "Singular System": 3, "Singular Company": 3,
        "Singular Country": 3, "Multiple Countries": 3, "Industry/Sector": 3,
        "Platform/Service": 2, "Drive-by": 3, "ICS": 1
    },
    "Phishing Campaign": {
        "Unknown/NA": 2, "Singular System": 2, "Singular Company": 2,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 2, "ICS": 1
    },
    "0-Day Vulnerability Exploitation": {
        "Unknown/NA": 5, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 5, "Multiple Countries": 5, "Industry/Sector": 5,
        "Platform/Service": 1, "Drive-by": 5, "ICS": 1
    },
    "Vulnerability Exploitation (CVE ≥ 9)": {
        "Unknown/NA": 5, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 5, "Multiple Countries": 5, "Industry/Sector": 5,
        "Platform/Service": 1, "Drive-by": 5, "ICS": 1
    },
    "APT / Threat Actor Activity": {
        "Unknown/NA": 1, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 1, "ICS": 1
    },
    "Persistent Backdoor / C2": {
        "Unknown/NA": 1, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 1, "ICS": 1
    },
    "Data Exfiltration": {
        "Unknown/NA": 1, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 1, "ICS": 1
    },
    "Ransomware": {
        "Unknown/NA": 1, "Singular System": 1, "Singular Company": 1,
        "Singular Country": 1, "Multiple Countries": 1, "Industry/Sector": 1,
        "Platform/Service": 1, "Drive-by": 1, "ICS": 1
    }
}
 