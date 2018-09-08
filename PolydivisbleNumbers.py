#   Strip Comments - CodeWars
#   Nilton Gomes Martins Junior
#   08/09/2018
#   https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

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
    if n == 1:
        return 0
    candidate = 1
    num_poly = 1
    while True:
        if is_polydivisible(str(candidate), b):
            num_poly += 1
            if num_poly == n:
                return str(candidate)
            candidate += 1
            print(candidate)

def main():
    print(get_polydivisible(22 ,10))
    return

if __name__ == "__main__":
    main()
