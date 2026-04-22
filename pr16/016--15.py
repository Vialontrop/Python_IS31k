import re
text = "hello world python"
print(re.sub(r"\b\w", lambda m: m.group().upper(), text))