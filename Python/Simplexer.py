#   Simplexer - Codewars
#   Nilton Gomes Martins Junior
#   28/01/2021
#   https://www.codewars.com/kata/54b8204dcd7f514bf2000348/train/python

class Simplexer(object):

    def __init__(self, expression):
        self.tokens = tokenize(expression)
        self.items_count = 0
        
    
    def __iter__(self):
        self.index = 0
        return self
                
    def __next__(self):
        if self.index == self.items_count - 2:
            raise StopIteration
        else:
            self.index += 1
            return self.tokens[self.index]
    
    @staticmethod
    def tokenize(expression):
        operator_tokens = ['+', '-', '*', '/', '%', '(', ')', '=']
        keyword_tokens = ['if', 'else', 'for', 'while', 'return', 'func', 'break']
