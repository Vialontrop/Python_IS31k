import re
text = "192.168.1.1"
pattern = r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}"
print(bool(re.fullmatch(pattern, text)))