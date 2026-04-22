import re
text = "apple, banana orange,grape"
print(re.split(r"[ ,]+", text))