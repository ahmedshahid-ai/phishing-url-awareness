# Test Results

**Project:** EWB Phishing URL Awareness Checker  
**Author:** Ahmed Shahid  
**Python version:** 3.15
**Operating system:** Windows
**Test date:** 2026-10-29



|#|Input|Expected result|Actual result|Pass/Fail|
|-|-|-|-|-|
|1|`https://www.example.com/login`|No listed warning signs; not proof of safety|No listed warning signs found. This does NOT prove safety.|PASS|
|2|`http://192.0.2.10/account`|IP address + HTTP|Uses an IP address instead of a familiar domain. Uses HTTP. HTTPS alone does not prove trust.|PASS|
|3|`http://example.com@sample.invalid/login`|`@` symbol + HTTP|Contains an `@` symbol; inspect carefully. Uses HTTP. HTTPS alone does not prove trust.|PASS|
|4|`https://a.b.c.d.e.example.invalid/path`|Many hostname segments|Contains many hostname segments/subdomains.|PASS|
|5|`https://xn--example.invalid/`|Punycode-style hostname|Contains a punycode-style hostname.|PASS|

## Notes

From this testing, I learned how to compare the expected result with the actual output of my program and decide whether a test passed or failed. I also learned that one URL can contain more than one warning sign. What surprised me most was that a URL could show no listed warning signs without being guaranteed safe. This helped me understand that my program checks only a few selected clues and cannot give a final decision about a URL's safety.

