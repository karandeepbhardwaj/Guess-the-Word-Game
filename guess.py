from game import Game

gameList = []
game_object = Game(0)
welcome_message1 = """
############################################################
#             Welcome To the Game of Thesaurus             #
############################################################

-+
-+ This the the great guessing game
-+"""
correct_guess_message = """
#############################
#        Correct Guess      #
#############################"""
incorrect_guess_message = """
###############################
#        Incorrect Guess      #
###############################"""


class Guess:

    def __init__(self):
        self.count_of_game = 0

    def main(self):
        self.menu()

    def menu(self):
        global game_object
        print(welcome_message1)

        while True:
            if not game_object.game_still_going:
                gameList.append(game_object)
                self.count_of_game = self.count_of_game + 1
                game_object = Game(self.count_of_game)

            print("""
current word: %s
Guess the word:\t%s
--Options----------------------------------------------------
+ G = Guess,  T = tell me,  L for a letter  ,and Q for quit +
-------------------------------------------------------------
""" % (game_object.word, game_object.get_printable_string()))
            answer = input("So what would you like to do? (g/t/l/q)\n")
            if answer == "g" or answer == "G":
                guessed_word = input("Make a guess: \n")
                response = game_object.guess_the_word(guessed_word)
                if response == "Y":
                    print(correct_guess_message)
                    pass
                    # update game data
                elif response == "N":
                    print(incorrect_guess_message)
                    pass

            if answer == "t" or answer == "T":
                print("The word was :" + game_object.word)
                game_object.tell_me()
                pass

            if answer == "l" or answer == "L":
                guessed_char = input("Enter a guess\n")
                game_object.guess_the_letter(guessed_char)
                pass

            if answer == "q" or answer == "Q":
                quit_choice = input("\nAre you sure? (y/n)\n")
                if quit_choice == "y" or quit_choice == "Y":
                    self.generate_report()
                    exit()
                else:
                    print("\n")
                    pass

    def generate_report(self):
        print("Game\tWord\tStatus\tBad Guesses\tMissed Letters\tScore")
        print("\n----\t----\t------\t-----------\t--------------\t-----\n")
        for game in gameList:
            print(game.game_number + 1, "\t", game.word, "\t", game.status, "\t",
                  game.bad_guesses, "\t", game.missed_letter, "\t", game.score)


g = Guess()
g.main()
