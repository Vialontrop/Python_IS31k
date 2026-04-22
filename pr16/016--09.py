import re
text = "Password1"
print(bool(re.fullmatch(r"(?=.*\d).{8,}", text)))