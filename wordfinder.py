from random import choice
class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Creates WordFinder from path"""

        file = open(path)
        self.word_list = self.find_words(file)
        print(f"{len(self.word_list)} words read")

    def __repr__(self):
        return f"<WordFinder words_list = {self.word_list}>"

    def find_words(self, file):
        """Reads file given a path strips off line breaks"""

        return [line.strip() for line in file]

    def random(self):
        """Chooses random word from word list"""

        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: finds only words omits comments and new lines"""

    def find_words(self, file):
        """Finds words that are not comments and not new lines, sets words_list"""

        self.word_list = [word for word in super().find_words(file) if not word.startswith("#") and word != '']
        return self.word_list


