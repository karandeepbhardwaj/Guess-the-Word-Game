from stringDatabase import StringDatabase

frequency = {"a": 8.17, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.70, "f": 2.23, "g": 2.02,
             "h": 6.09, "i": 6.97, "j": 0.15, "k": 0.77, "l": 4.03, "m": 2.41, "n": 6.75,
             "o": 7.51, "p": 1.93, "q": 0.10, "r": 5.99, "s": 6.33, "t": 9.06, "u": 2.76,
             "v": 0.98, "w": 2.36, "x": 0.15, "y": 1.97, "z": 0.07}


class Game:

    def __init__(self, game_number, status="", bad_word_guesses=0, bad_letter_guesses=0, missed_letter=0, score=0.0, game_still_going=True):

        self.game_number = game_number
        self.word = StringDatabase().get_random()
        self.status = status
        self.bad_word_guesses = bad_word_guesses
        self.bed_letter_guesses = bad_letter_guesses
        self.letter_found_count = 0
        self.missed_letter = missed_letter
        self.score = score
        self.game_still_going = game_still_going
        self.new_guess_string = ["-", "-", "-", "-"]
        self.inner_count = 0
        self.total_letters = 0

    def guess_the_word(self, guessed_word):
        if guessed_word == self.word:
            print(self.get_value_of_hidden_chars())
            self.status = "Success"
            self.game_still_going = False
            return "Y"
        else:
            self.bad_word_guesses += 1
            return "N"

    def tell_me(self):
        response = []
        for i in range(len(self.word)):
            if self.new_guess_string[i] != self.word[i]:
                response.append(self.get_score_of_word(self.word[i]))
        for x in response:
            self.score += x
        print("score:", self.score*-1)
        self.status = "Gave Up"
        self.game_still_going = False

    def guess_the_letter(self, guessed_char):
        for i in range(len(self.word)):
            if guessed_char == self.word[i]:
                self.new_guess_string[i] = guessed_char
                self.letter_found_count += 1
                self.total_letters += 1
        print("You found %d letter so far" % self.letter_found_count)
        if self.total_letters == 4:
            self.status = "Success"
            self.game_still_going = False
            print("You guessed the word!")

    def get_printable_string(self):
        new = ""
        for x in self.new_guess_string:
            new += x
        return new

    def get_score_of_word(self, character):
        for i in frequency.keys():
            if character == i:
                return frequency[i]

    def get_value_of_hidden_chars(self):
        response = []
        for i in range(len(self.word)):
            if self.new_guess_string[i] != self.word[i]:
                response.append(self.get_score_of_word(self.word[i]))
        for x in response:
            self.score += x
        return self.score
