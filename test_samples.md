# Test Results

Python version used: 3.10 | Operating system: Windows
Date: 27 October 2026

Name Ahmed Shahid

|#|Input|Expected result|Actual result|Pass/Fail|
|-|-|-|-|-|
|1|`https://www.example.com/login`|No listed warning signs|No listed warning signs found. This does NOT prove safety.|PASS|
|2|`http://192.0.2.10/account`|IP address + HTTP|Uses an IP address instead of a familiar domain. <br> Uses HTTP. HTTPS alone does not prove trust.|PASS|
|3|`http://example.com@sample.invalid/login`|@ symbol + HTTP|Contains an @ symbol; inspect carefully. <br> Uses HTTP. HTTPS alone does not prove trust.|PASS|
|4|`https://a.b.c.d.e.example.invalid/path`|Many hostname segments|Contains many hostname segments/subdomains.|PASS|
|5|`https://xn--example.invalid/`|Punycode-style hostname|Contains a punycode-style hostname.|PASS|

## Notes

Building this tool showed me how easily a malicious link can hide behind technical tricks. I was most surprised by how the `@` symbol makes a browser ignore the first part of the URL, and how quickly the script can flag these indicators without ever actually opening the connection.

