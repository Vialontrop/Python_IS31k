import string

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

clean_text = text.translate(str.maketrans("", "", string.punctuation))

with open("clean.txt", "w", encoding="utf-8") as f:
    f.write(clean_text)
