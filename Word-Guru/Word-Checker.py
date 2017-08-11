import sys
import os

class WordChecker():
    def __init__(self):
        # Replace with correct filepath
        self.filepath = ".../Word-Guru/GermanWords/Words.txt"
        self.via_shell = True
        self.word = None
        self.letters = []
        self.possible_words = []
        self.dictionary = []
        self.len_of_output = 0

        self.start_check()

    def parse_input(self):
        if self.via_shell:
            self.letters = []
            self.len_of_output = int(sys.argv[-1])
            for i in range(0, len(sys.argv[1])):
                self.letters.append(str(sys.argv[1][i]).lower())
        if not self.via_shell:
            self.letters = []
            for i in range(0, len(self.word)):
                self.letters.append(self.word[i].lower())

    def parse_words(self):
        with open(self.filepath, encoding="utf8") as file:
            content = file.readlines()

        content = [x.strip() for x in content]
        self.dictionary = content

    def check_word_for_letters(self, word, characters):
        word = word.lower()
        length_word = len(word)
        identical_letters = 0
        letters = characters[:]
        for character in word:
            for letter in letters:
                if character == letter:
                    identical_letters += 1
                    letters.remove(letter)
                    break
        if length_word == identical_letters:
            return True
        return False

    def check_all_words(self, words):
        for word in words:
            if self.len_of_output == 0:
                if self.check_word_for_letters(word, self.letters):
                    self.possible_words.append(word)
            if len(word) == self.len_of_output:
                if self.check_word_for_letters(word, self.letters):
                    self.possible_words.append(word)


    def draw_output(self):
        os.system("cls")
        sorted_words = [word.lower() for word in sorted(self.possible_words)]
        output = ", ".join(sorted_words)
        print(output)

    def start_check(self):
        self.parse_input()
        self.parse_words()
        self.check_all_words(self.dictionary)
        self.draw_output()

WordChecker()
