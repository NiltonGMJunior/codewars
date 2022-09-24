#   Calculator   -   CodeWars
#   Nilton Gomes Martins Junior
#   05/06/2021
#   https://www.codewars.com/kata/5235c913397cbf2508000048/train/python

class Calculator(object):
    def evaluate(self, string):
        # This assumes the string contains a valid expression using only the +, -, * and / operators.
        exp = list(string.replace(' ', ''))

        # Divisions
        while '/' in exp:
            idx = exp.index('/')
            res = int(exp[idx - 1]) / int(exp[idx + 1])
            exp[idx - 1 : idx + 2] = str(res)
        
        # Multiplications
        while '*' in exp:
            idx = exp.index('*')
            res = int(exp[idx - 1]) * int(exp[idx + 1])
            exp[idx - 1 : idx + 2] = str(res)

        # Additions
        while '+' in exp:
            idx = exp.index('+')
            res = int(exp[idx - 1]) + int(exp[idx + 1])
            exp[idx - 1 : idx + 2] = str(res)

        # Subtractions
        while '-' in exp:
            idx = exp.index('-')
            res = int(exp[idx - 1]) - int(exp[idx + 1])
            exp[idx - 1 : idx + 2] = str(res)

        return int(exp[0])
    
def main():
    print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"))

if __name__ == "__main__":
    main()
