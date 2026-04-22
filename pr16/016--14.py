import re
text = "hello hello world"
print(re.findall(r"\b(\w+) \1\b", text))