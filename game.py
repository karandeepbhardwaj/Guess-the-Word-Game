from stringDatabase import StringDatabase

frequency = {"a": 8.17, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.70, "f": 2.23, "g": 2.02,
             "h": 6.09, "i": 6.97, "j": 0.15, "k": 0.77, "l": 4.03, "m": 2.41, "n": 6.75,
             "o": 7.51, "p": 1.93, "q": 0.10, "r": 5.99, "s": 6.33, "t": 9.06, "u": 2.76,
             "v": 0.98, "w": 2.36, "x": 0.15, "y": 1.97, "z": 0.07}


class Game:
    """Class Game : This class handles the game play for one game and stores data related to just one game
                    at a time. The class's object is created in the guess class and then data manipulation
                    on the variables are done in order to maintain the score and handle function calls.
                    This is followed by an indented block of statements which form the body of the class.
                    Eight methods have been defined in the class."""

    def __init__(self, game_number, status="", bad_word_guesses=0, bad_letter_guesses=0, missed_letter=0, score=0.0,
                 game_still_going=True):
        """The __init__ method: This method is similar to constructors in C++ and Java.
                                It is run as soon as an object of a class is instantiated.
                                The method is used to do all initializations required to be done with object.
                                :param game_number: Keeps the count of the games being played by player
                                :param status: Keeps the condition of th game which is either success or Gave up,
                                                which is string.
                                :param bad_word_guesses: Keeps the count of the number of the incorrect guesses player
                                                         makes while guessing the whole word.
                                :param bad_letter_guesses: Keeps the count of the number of the incorrect guesses player
                                                            makes while guessing the one letter at a time.
                                :param missed_letter: This keeps the count of the letters that player was unable to
                                                        guess say if he made a bad guesses and gave up or he chose tell me
                                                        option, this will have the value of the letters user was not able
                                                        to guess.
                                :param score: This keeps the total score of the game being played, is accessed by each method
                                              in the class to update the score of the player.
                                :param game_still_going: This is a boolean variable which keeps the status of the game
                                                        is whether still going or has finished. Returns True or False.
                                                        Changes when game is finished and is further used in guess class
                                                        to know that the game has ended and start a new game by storing
                                                        previous games score."""
        self.game_number = game_number
        self.word = "case"
        self.status = status
        self.bad_word_guesses = bad_word_guesses
        self.bed_letter_guesses = bad_letter_guesses
        self.letter_found_count = 0
        self.letter_not_found_count =0
        self.missed_letter = missed_letter
        self.score = score
        self.game_still_going = game_still_going
        self.new_guess_string = ["-", "-", "-", "-"]
        self.total_letters = 0
        self.letter_give_count = 0
        self.local_char = []

    def guess_the_word(self, guessed_word):
        """guess_the_word : This method is used in guess class when user chooses the option to guess the whole word.
                            If he makes a right or wring guess, this method returns the result to guess class
                            and stores the values fot record of the score. This method returns the string "Y" or "N"
        :param guessed_word: This variable is word input by user and is matched with the word currently used by
                            the game.
        :return: String to specify the result of the match.
        """
        if guessed_word == self.word:
            self.status = "Success"
            self.game_still_going = False
            self.score = self.get_value_of_found_chars()
            return "Y"
        else:
            self.bad_word_guesses += 1
            return "N"

    def tell_me(self):
        """tell_me : This method is handles the tell me option of the game. If user calls to tell the word,
                    This method returns prints the word on the screen and stores the calculated score in the
                    data maintained."""
        self.status = "Gave Up"
        self.game_still_going = False

    def guess_the_letter(self, guessed_char):
        """guess_the_letter : This method is called when the user decides to guess the letter instead of
                                whole word. It takes the guessed character from the user as argument,
                                compares it with the each letter in the game word and returns result
                                and records the result accordingly.
        :param guessed_char: This the input given by the user on the screen to be matched with all the
                            letters in the word.
        :return: Return message if user typing already guessed word again
        """
        num_correct = 0
        if guessed_char in self.local_char:
            print("You have already guessed this word")
            return
        for i in range(len(self.word)):
            if guessed_char == self.word[i]:
                num_correct += 1
                self.new_guess_string[i] = guessed_char
                self.letter_found_count += 1
                self.total_letters += 1
                self.local_char.append(guessed_char)
                self.score += self.get_score_of_word(self.word[i])
        print("You found %d letter so far" % self.letter_found_count)

        if num_correct == 0:
            self.missed_letter += 1

        if self.total_letters == 4:
            self.status = "Success"
            self.game_still_going = False
            print("You guessed the word!")
        self.letter_give_count += 1

    def get_printable_string(self):
        """get_printable_string :  This method displays the string in a way that each time if the
                                    user guesses a correct letter, it will return the correct letters
                                    and keep "-"  on the places where user has not guessed the letters.
        :return: String "new", which is the string in the program desired format.
        """
        new = ""
        for x in self.new_guess_string:
            new += x
        return new

    def get_score_of_word(self, character):
        """get_score_of_word : This method iterates through the frequency list of all the English alphabets
                                and returns the value of the alphabet requested for.
        :param character: Is the character for which the value is requested and is to be searched from the
                            frequency list.
        :return: Value of the character decided.
        """
        for i in frequency.keys():
            if character == i:
                return frequency[i]

    def get_value_of_not_found_chars(self):
        """get_value_of_not_found_chars : This method calculates the score of the letters which have been not
                                            yet found by the user. It searches the list and adds the value of the letters
                                            that are still covered.
        :return: Float value of total of the alphabets those are still covered.
        """
        response = []
        temp_score = 0.0
        for i in range(len(self.word)):
            if self.new_guess_string[i] != self.word[i]:
                response.append(self.get_score_of_word(self.word[i]))
        for x in response:
            temp_score += x
        return temp_score

    def get_value_of_found_chars(self):
        """get_value_of_found_chars : This method calculates the score of the letters which have been found by the user.
                                        It searches the list and adds the value of the letters that are uncovered.
        :return: Float value of total of the alphabets those are uncovered.
        """
        response = []
        temp_score3 = 0.0
        for i in range(len(self.word)):
            if self.new_guess_string[i] == self.word[i]:
                response.append(self.get_score_of_word(self.word[i]))
        for x in response:
            temp_score3 += x
        return temp_score3

    def final_score(self):
        """final_score :  This method calculates the final score of the user after he has either guessed the whole word
                            or has given up. It takes all the criteria in account and calculates the score by taking
                            rules. Stores the value in the score variable.
        :return: no return.
        """

        temp_score = self.score

        if self.status == "Gave Up":
            return self.get_value_of_not_found_chars() * -1

        if self.letter_give_count > 0:
            temp_score /= self.letter_give_count

        if self.bad_word_guesses > 0:
            for x in range(self.bad_word_guesses):
                temp_score = temp_score * 0.90

        return temp_score
