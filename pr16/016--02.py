import re
text = "There are 12 apples and 5 bananas"
print(re.findall(r"\d+", text))