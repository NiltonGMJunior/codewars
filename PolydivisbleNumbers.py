#   Polydivisble Numbers - CodeWars
#   Nilton Gomes Martins Junior
#   08/09/2018
#   https://www.codewars.com/kata/polydivisible-numbers/python

#   NOTE:   is_polydivisble is workink properly
#   TODO:   get_polydivisible should return number in the base b, not decimal (up to base 62)
#   TODO:   MAYBE - Implement function to convert string of number in one base to another base

def is_polydivisible(s, b):
    for i in range(len(s)):
        num = sum([int(n)*(b**(i - p)) for p, n in enumerate(s[:i + 1])])
        if num % (int(i) + 1) != 0:
            return False
    return True

def get_polydivisible(n, b):
    #   NOTE:   0 is always the first polydivisible number
    #

def main():
    print(get_polydivisible(22 ,10))
    return

if __name__ == "__main__":
    main()
