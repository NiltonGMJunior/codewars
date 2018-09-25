#   The learning game - Machine Learning #01 - CodeWars
#   Nilton Gomes Martins Junior
#   06/09/2018
#   http://www.codewars.com/kata/the-learning-game-machine-learning-number-1/train/python

ACTIONS =   {   0   :   lambda  x   :   x   +   1,
                1   :   lambda  x   :   0,
                2   :   lambda  x   :   x   /   2,
                3   :   lambda  x   :   x   *   100,
                4   :   lambda  x   :   x   %   2
            }

class Machine:
    def __init__(self, tokens={}, generation=0):
        self.tokens = tokens
        self.generation = generation
    def command(self, cmd, num):
        
    def response(self, res):
        self.tokens += 1 if res else self.tokens -=1
        self.generation += 1

def main():
    return

if __name__ == "__main__":
    main()
