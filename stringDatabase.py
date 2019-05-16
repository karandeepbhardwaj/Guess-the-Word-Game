import random


class StringDatabase:

    def __init__(self):
        self.words = []
        for l in open("four_letters.txt").readlines():
            self.words = self.words + l.rstrip("\r\n").split(" ")

    def get_random(self):
        random_line = random.choice(self.words)
        return random_line
