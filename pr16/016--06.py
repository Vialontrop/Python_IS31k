import re
text = "Apple and banana are amazing"
print(re.findall(r"\b[aA]\w*", text))