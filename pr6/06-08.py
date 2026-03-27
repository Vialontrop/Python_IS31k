class WordCaseSeparator:
    def __init__(self):
        self.upper_words = []
        self.lower_words = []

    def add_word(self, word):
        if word[0].isupper():
            self.upper_words.append(word)
        else:
            self.lower_words.append(word)

    def upper_case_words(self):
        return self.upper_words

    def lower_case_words(self):
        return self.lower_words
ws = WordCaseSeparator()
ws.add_word("Apple")
ws.add_word("banana")
ws.add_word("Cherry")
print("С заглавной:", ws.upper_case_words())
print("Со строчной:", ws.lower_case_words())