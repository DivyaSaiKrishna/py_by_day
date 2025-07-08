import math
import random

class passwordGene:
    def __init__(self, salt):
        self.salt = salt

    def genPass(self):
        random.seed(self.salt)
        return random.random()

if __name__ == "__main__":

    passwordC = passwordGene(4)
    print(passwordC.genPass())
