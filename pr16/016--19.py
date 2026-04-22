import re
text = "Name: John Age: 25"
m = re.search(r"Name: (\w+) Age: (\d+)", text)
print(m.groups())