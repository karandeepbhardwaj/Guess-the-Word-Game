from game import Game

gameList = []  # This List Stores the object of the class game which helps in creating multiple
# which helps to maintain the score of all the games being played by the user.
game_object = Game(0)  # Object of the class Game to be used to store data of all the games being
# played by the user.
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
    """Class Guess : This class is defined 3 methods and is the main interaction with the user.
                     This is followed by an indented block of statements which form the body of the class.
                    three methods have been defined in the class. This class controls the flow of the game
                    creates new game stores the previous game object in the game List variable. Also displays the
                    menu to the user to interact with the application. This works as a view class which updates the
                    screen according to the manipulation of the data being done at the back ground."""

    def __init__(self):
        """The __init__ method: This method is similar to constructors in C++ and Java.
                                It is run as soon as an object of a class is instantiated.
                                The method is used to do all initializations required to be done with object."""
        self.count_of_game = 0

    def main(self):
        """main : This the main method of the class runs when is called and runs all the methods called inside it.
                  Main function is the entry point of any program. But python interpreter executes the source file code
                  sequentially and doesn’t call any method if it’s not part of the code.
                  But if it’s directly part of the code then it will be executed when the file is imported as a module.
        :return: No return.
        """
        self.menu()

    def menu(self):
        """menu : This Method is the view point for user, it displays all the game interface, lets the user interact
                    with it by taking inputs and giving results on the console screen. This method furthers has associations
                    with method defined in the game class which are called by using the object of the class.
                    This method keeps repeating until user chooses to quit the game. It further has options like:
                    guess :  Lets user guess the the whole word.
                    tell me :  lets user give up and display the word on the screen
                    letter : Lets user uncover the hidden letter by making a guess.
                    quit : Ends the infinity loop and display the result on the screen.
        :return: no return.
        """
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
        """generate_report :  This method takes the score stored in the game list of each object
                                and displays the result in required format. Prints the output on the screen.
                                takes values from every variable of game class required to give information of the
                                each game for each word.
        :return: no returns.
        """
        print("Game\t Word\t Status\t\t Bad Guesses\t Missed Letters\t Score")
        print("----\t ----\t -------\t -----------\t --------------\t -----")
        for game in gameList:
            print(game.game_number + 1," ", "\t", game.word, "\t", game.status, "\t",
                  game.bad_word_guesses,"          ", "\t", game.missed_letter, "\t\t\t\t", game.score)


g = Guess()
g.main()
