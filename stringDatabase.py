import random


class StringDatabase:
    """StringDatabase : This class is the input output handling class, the main purpose is to take word from the
                        text file, store it in required data structure which in this code's case is string"""

    def __init__(self):
        """The __init__ method: This method is similar to constructors in C++ and Java.
                                It is run as soon as an object of a class is instantiated.
                                The method is used to do all initializations required to be done with object."""
        self.words = []
        for l in open("four_letters.txt").readlines():
            self.words = self.words + l.rstrip("\r\n").split(" ")

    def get_random(self):
        """get_random : This method calls the internal function of python language and returns a random string
                        from the variable.
        :return: String selected at random by the random function.
        """
        random_line = random.choice(self.words)
        return random_line
