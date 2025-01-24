from urllib.parse import urlparse

def filter_email(email, url_list, white_list=None):
    # Extract the domain part from the email
    email_domain = email.split('@')[1].lower()

    def normalize_domain(domain):
        """Normalize a domain by removing 'www.' and handling subdomains."""
        return domain.replace('www.', '').strip().lower()

    # Normalize email domain
    email_domain_parts = email_domain.split('.')

    # Compare email domain with each URL in the list
    for url in url_list:
        parsed_url = urlparse(url)
        url_domain = normalize_domain(parsed_url.netloc)

        # Check if email domain matches URL domain or subdomain
        if email_domain == url_domain:
            return True
        
        # Check if the root domain matches (ignoring TLD)
        url_root_domain = '.'.join(url_domain.split('.')[:-1])  # Remove TLD
        if email_domain.startswith(url_root_domain):
            return True
        
        if len(email_domain_parts) > 1 and len(url_domain.split('.')) > 1 and email_domain_parts[-2:] == url_domain.split('.')[-2:]:
            return True

    # Check white list for additional matches
    if white_list:
        for allowed_domain in white_list:
            allowed_domain_normalized = normalize_domain(allowed_domain)

            # Check if email domain matches the white list domain
            if email_domain == allowed_domain_normalized:
                return True
            
            # Check if the root domain matches (ignoring TLD)
            allowed_root_domain = '.'.join(allowed_domain_normalized.split('.')[:-1])  # Remove TLD
            if email_domain.startswith(allowed_root_domain):
                return True
            
            if len(email_domain_parts) > 1 and len(allowed_root_domain.split('.')) > 1 and email_domain_parts[-2:] == allowed_root_domain.split('.')[-2:]:
                return True

    return False

# Example usage
if __name__ == "__main__":
    email = "pierluigi.paganini@com"
    url_list = [
        "https://securityaffairs.com/172864/hacktivism/ukrainian-cyber-alliance-destroyed-russian-isp-nodex.html"    ]
    white_list = ["securityaffairs.com"]

    result = filter_email(email, url_list, white_list=white_list)
    print(f"Email {email} is filtered: {result}")
