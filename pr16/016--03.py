import re
text = "test@example.com"
print(bool(re.fullmatch(r"[\w.-]+@[\w.-]+\.\w+", text)))