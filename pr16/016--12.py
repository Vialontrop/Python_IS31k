import re
text = "<p>Hello</p>"
print(re.sub(r"<.*?>", "", text))