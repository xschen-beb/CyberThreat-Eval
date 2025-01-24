import ast

def process_mitre_ttps(key, value):
    """
    Processes the MITRE TTPs field and formats the output.
    """
    text_output = ""
    
    if not value:
        text_output += f"#### {key} \n - No TTPs provided.\n\n"
        return text_output

    formatted_ttps = []
    
    # Check and parse value
    try:
        if isinstance(value, str):
            data = ast.literal_eval(value)  # Convert string to dict/list
        else:
            data = value  # Already a dict or list
    except Exception as e:
        text_output += f"#### {key} \n - Error parsing TTPs: {str(e)}\n\n"
        return text_output

    if isinstance(data, dict):  # If TTPs are a dictionary
        for ttp_id, details in data.items():
            try:
                # Split details into description, confidence, and justification
                parts = details.split(', Confidence: ')
                description = parts[0].strip()
                confidence_justification = parts[1].split('. Justification: ')
                confidence = confidence_justification[0].strip()
                justification = confidence_justification[1].strip()
                
                formatted_ttps.append(
                    f"- {ttp_id}: {description};\n  Confidence: {confidence}.\n  Justification: {justification}"
                )
            except IndexError:
                formatted_ttps.append(f"- {ttp_id}: {details};\n  Confidence: Not specified.\n  Justification: Not specified")
    elif isinstance(data, list):  # If TTPs are a list of dictionaries
        for ttp in data:
            for ttp_id, details in ttp.items():
                try:
                    parts = details.split(', Confidence: ')
                    description = parts[0].strip()
                    confidence_justification = parts[1].split('. Justification: ')
                    confidence = confidence_justification[0].strip()
                    justification = confidence_justification[1].strip()
                    
                    formatted_ttps.append(
                        f"- {ttp_id}: {description};\n  Confidence: {confidence}.\n  Justification: {justification}"
                    )
                except IndexError:
                    formatted_ttps.append(f"- {ttp_id}: {details};\n  Confidence: Not specified.\n  Justification: Not specified")
    else:  # Unsupported data type
        text_output += f"#### {key} \n - Unsupported TTP format: {data}\n\n"
        return text_output

    # Add formatted TTPs to text output
    text_output += f"#### {key} \n" + "\n".join(formatted_ttps) + "\n"
    return text_output

# Example usage
if __name__ == '__main__':
    key = "MITRE TTPs"
    value = """{
        "T1078": "Valid Accounts, Confidence: Medium. Justification: The report mentions weak authentication as a vulnerability, which aligns with the use of valid accounts for unauthorized access.",
        "T1071": "Application Layer Protocol, Confidence: Medium. Justification: The report highlights the need for secure communications, indicating that attackers may exploit insecure communication protocols.",
        "T1496": "Resource Hijacking, Confidence: Low. Justification: The report discusses the importance of secure controls to thwart malicious commands, which could be related to resource hijacking."
    }"""
    print(process_mitre_ttps(key, value))
