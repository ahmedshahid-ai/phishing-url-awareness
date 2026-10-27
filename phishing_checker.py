import re
from urllib.parse import urlparse

INFO_MESSAGES = ("No URL entered", "Could not identify", "No listed warning", "This text is not")

def has_warnings(findings):
    """Helper function to check if findings contain actual warnings."""
    return not findings[0].startswith(INFO_MESSAGES)

def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []
    
    if not url:
        return ["No URL entered."]
        
    candidate = url if "://" in url else "http://" + url
    
    # Improvement C: Stop crashes on malformed input
    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]
        
    host = (parsed.hostname or "").lower()
    
    if not host:
        return ["Could not identify a hostname."]
        
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")
        
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")
        
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")
        
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")
        
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")
        
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")
        
    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")
        
    return findings

def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only — this program does not open URLs.")
    
    # Improvement A: Loop with quit command
    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break
            
        print("\nResult:")
        findings = inspect_url(raw_url)
        for item in findings:
            print("- " + item)
            
        # Improvement B: Review carefully summary
        if has_warnings(findings):
            print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")
            
        print("Never enter passwords from unexpected links.")

if __name__ == "__main__":
    main()
