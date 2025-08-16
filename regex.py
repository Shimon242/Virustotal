import re

text = 'some log line with "malicious": 48 in it'

# Use regex to find the number after "malicious":
match = re.search(r'"malicious":\s*(\d+)', text)

if match:
    number = int(match.group(1))
    print(number)  # 48
