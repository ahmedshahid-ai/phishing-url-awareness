# EWB Phishing URL Awareness Checker

## Overview
Phishing is a deceptive tactic where attackers use fake links or messages to trick individuals into revealing sensitive information like passwords or bank details. This Python command-line tool acts as a first line of defense by strictly inspecting the text of a provided URL for common, visible phishing indicators without ever visiting the site.

## Features
- Detects an `@` symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (`xn--`)
- Flags the HTTP scheme
- **Looping Capability:** Users can check multiple URLs in a single session without restarting the program.
- **Review Summary:** Calculates and prints a summary of total warning signs found for quick assessment.
- **Crash Prevention:** Safely handles malformed input to prevent program crashes.

## Requirements
Python 3.10 or later. No extra packages.

## How to Run
Windows: `python phishing_checker.py`
Mac/Linux: `python3 phishing_checker.py`

## Example Output
```text
EWB Phishing URL Awareness Checker
Text checks only — this program does not open URLs.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Never enter passwords from unexpected links.
```

## Testing
| # | Input | Expected result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | Uses an IP address instead of a familiar domain. Uses HTTP. | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | Contains an @ symbol; inspect carefully. Uses HTTP. | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Contains many hostname segments/subdomains. | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Contains a punycode-style hostname. | PASS |

## Screenshots
![Sample run](screenshots/sample_run.png)
![Test results](screenshots/test_results.png)

## Improvements
1. **Continuous Looping:** I implemented a `while True` loop so the user can check multiple URLs sequentially and type 'q' to quit. I tested this by entering multiple sample URLs in one session and verifying the program didn't close until 'q' was pressed.
2. **Review Carefully Summary:** I created a `has_warnings` helper function that dynamically counts and prints the total number of warning signs found. I tested this by feeding it URLs with 0, 1, and 2 warning signs to ensure the count was accurate.
3. **Crash Prevention (Malformed Input):** Added a `try/except` block to safely catch `ValueError` exceptions if a user enters an unparseable URL (like `http://[bad`). Tested by entering broken syntax to ensure it returned a friendly error instead of crashing.

## Limitations
This is an educational tool. It only reads URL text. It does not visit URLs, scan for malware or prove that a URL is safe. "No warning signs found" does NOT mean a URL is safe.

## Ethical Use
Use sample strings only. Do not collect credentials. Do not use this project to deceive anyone or to test websites without permission.

## Author
Ahmed Shahid, AI-powered Cybersecurity, EWB Courses
