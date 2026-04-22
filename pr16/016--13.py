import re
text = "Visit https://example.com and http://test.com"
print(re.findall(r"https?://\S+", text))