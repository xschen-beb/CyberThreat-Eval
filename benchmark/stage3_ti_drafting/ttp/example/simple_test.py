"""
Simple test code for compute_raw_precision_recall function
Tests articles from example files with simulated LLM predictions
Calculates micro-averaged precision and recall
"""
import json
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

for path in [CURRENT_DIR, PARENT_DIR]:
    if path not in sys.path:
        sys.path.append(path)

from eval.compute import compute_raw_precision_recall, load_articles_from_file, load_results_from_file

# Load test data from example files
ground_truth_file = os.path.join(CURRENT_DIR, "example_ground_truth.json")
predicted_file = os.path.join(CURRENT_DIR, "example_predicted.json")
"""
Ground truth file:
[
    {
        "title": "DeepSeek Lure Using CAPTCHAs To Spread Malware",
        "content": "## Snapshot\r\nResearchers at ThreatLabz have identified a malware campaign that exploits the popularity of the DeepSeek AI chatbot through brand impersonation.\r\n\r\n## Description\r\nCybercriminals are using fake DeepSeek look-alike domains to distribute the Vidar information stealer, targeting users with a fake CAPTCHA page that injects a malicious PowerShell command into their clipboard. When the command is executed, it downloads the Vidar executable, which then steals sensitive data such as credentials, cryptocurrency wallet information, browser cookies, and personal files. The malware specifically searches for data related to cryptocurrency wallets and browser extensions within the victim's file system and registry.\r\n\r\nVidar conceals its command-and-control communication using legitimate services like Telegram and Steam. The campaign uses a malicious website that mimics DeepSeek, registered on January 31, 2025, to lure victims with a fake partner registration prompt. The Vidar malware harvests a wide range of data and uses legitimate platforms to exfiltrate the stolen information to attacker-controlled servers, which include several IP addresses and a publicly accessible Steam community profile.",
        "ttps": [
            "T1204 - User Execution",
            "T1189 - Drive-by Compromise",
            "T1036 - Masquerading"
        ],
        "source": "DeepSeek Lure Using CAPTCHAs To Spread Malware"
    },
    {
        "title": "Auto-Color: An Emerging and Evasive Linux Backdoor",
        "content": "## Snapshot\r\nPalo Alto Networks researchers discovered a new Linux malware named Auto-color, which employs advanced evasion techniques to avoid detection and grants threat actors full remote access to compromised machines.\r\n\r\n## Description\r\nThis malware disguises itself by renaming its file to benign-sounding names like \"door\" or \"egg,\" making it harder for security tools to identify. Once executed, Auto-color installs a malicious library, libcext.so.2, which hooks into core system libraries, allowing it to hide network activity and prevent removal. The malware also alters network activity data to conceal connections with its remote command-and-control (C2) servers, making it more difficult to detect its presence.\r\n\r\nAuto-color's custom encryption protocol helps hide the configuration details for these C2 servers, which are dynamically configured based on the target system. The malware supports various functions through a specialized API, including reverse shell creation, file manipulation, and using the infected machine as a proxy. It can also modify global payload configurations remotely, enabling attackers to maintain control over compromised systems. Auto-color's persistence is enhanced by modifying the /etc/ld.preload file, ensuring its malicious library is loaded before other system libraries. While its exact method of delivery remains unclear, Auto-color has been primarily used to target universities and government offices in North America and Asia.",
        "ttps": [
            "T1204 - User Execution",
            "T1036 - Masquerading",
            "T1070 - Indicator Removal",
            "T1219 - Remote Access Software"
        ],
        "source": "Auto-Color: An Emerging and Evasive Linux Backdoor"
    }
]
predicted file:
[
    {
        "T1204": "User Execution, Confidence: High. Justification: The article describes users executing malicious PowerShell commands from clipboard.",
        "T1189": "Drive-by Compromise, Confidence: High. Justification: The article mentions fake CAPTCHA pages and drive-by download techniques.",
        "T1036": "Masquerading, Confidence: High. Justification: The campaign uses fake DeepSeek look-alike domains to masquerade as legitimate services.",
        "T1071": "Application Layer Protocol, Confidence: Low. Justification: The article mentions communication via Telegram and Steam."  # False positive
    },
    {
        "T1036": "Masquerading, Confidence: High. Justification: The malware disguises itself with benign-sounding names like 'door' or 'egg'.",
        "T1070": "Indicator Removal, Confidence: High. Justification: The malware alters network activity data to conceal C2 connections.",
        "T1219": "Remote Access Software, Confidence: High. Justification: The malware provides remote access capabilities including reverse shell creation.",
        "T1055": "Process Injection, Confidence: Low. Justification: The article mentions hooking into system libraries."  # False positive
    }
]
"""
try:
    print(f"Loading ground truth articles from: {ground_truth_file}")
    test_article = load_articles_from_file(ground_truth_file)
    print(f"Loaded {len(test_article)} articles")
    
    print(f"Loading predicted results from: {predicted_file}")
    test_result = load_results_from_file(predicted_file)
    print(f"Loaded {len(test_result)} results")
    
    # Validate lengths match
    if len(test_article) != len(test_result):
        print(f"Warning: Number of articles ({len(test_article)}) does not match number of results ({len(test_result)})")
        print("Using the minimum length for evaluation")
        min_len = min(len(test_article), len(test_result))
        test_article = test_article[:min_len]
        test_result = test_result[:min_len]
        
except Exception as e:
    print(f"Error loading test files: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Run tests
print("=" * 60)
print("Simple Test for compute_raw_precision_recall")
print("Testing Multiple Articles with Metrics")
print("=" * 60)

# Display article information
for i, (article, result) in enumerate(zip(test_article, test_result), 1):
    print(f"\nArticle {i}: {article['title']}")
    print(f"  Ground Truth TTPs: {article['ttps']}")
    # result is a JSON string, parse it to get the keys
    try:
        if isinstance(result, str):
            predicted_ttps = list(json.loads(result).keys())
        else:
            predicted_ttps = list(result.keys())
        print(f"  Predicted TTPs: {predicted_ttps}")
    except Exception as e:
        print(f"  Error parsing predicted TTPs: {e}")

# Use compute_raw_precision_recall to calculate micro-averaged metrics
# Pass all articles and all results as lists
print("\n" + "=" * 60)
print("Processing all articles using compute_raw_precision_recall...")
print("=" * 60)

try:
    # compute_raw_precision_recall now supports a list of results (one per article)
    micro_precision, micro_recall = compute_raw_precision_recall(test_article, test_result)
    
    # Calculate F1 score
    micro_f1 = 2 * (micro_precision * micro_recall) / (micro_precision + micro_recall) if (micro_precision + micro_recall) > 0 else 0
    
    print("\n" + "=" * 60)
    print("Micro-Averaged (Aggregated) Results")
    print("=" * 60)
    print(f"Micro-Averaged Precision: {micro_precision:.4f}")
    print(f"Micro-Averaged Recall: {micro_recall:.4f}")
    print(f"Micro-Averaged F1-Score: {micro_f1:.4f}")
    print("=" * 60)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

