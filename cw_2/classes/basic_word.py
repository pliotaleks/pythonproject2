class BasicWord:
    def __init__(self, init_word, subwords):
        self.init_word = init_word
        self.subwords = subwords

    def check_word(self, word):
        return word in self.subwords

    def count_subwords(self):
        return len(self.subwords)

    def __repr__(self):
        return f"<BasicWord object. Args: init_word: {self.init_word}, subwords: {self.subwords}>"


basic_word = BasicWord("word", ["wot", "rdw"])

# print(basic_word.init_word)
# print(basic_word.subwords)
print(basic_word)
