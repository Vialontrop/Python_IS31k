from collections import Counter

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()
    words = text.split()

counter = Counter(words)

for word, count in counter.most_common():
    print(word, count)
