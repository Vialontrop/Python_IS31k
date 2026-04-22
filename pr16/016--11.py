import re
text = "I am at home in my big house"
print(re.sub(r"\b\w{1,2}\b", "***", text))