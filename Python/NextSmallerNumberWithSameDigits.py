#   Next smaller number with the same digits - CodeWars
#   Nilton Gomes Martins Junior
#   30/08/2018
#   https://www.codewars.com/trainer/python

from itertools import permutations

def next_smaller(n):
    # OPTIMIZE: Timing out in CodeWars
    perm = sorted([int(''.join(x)) for x in list(filter(lambda x : int(''.join(x)) < n, permutations(str(n))))])
    return perm[-1] if perm else -1

def main():
    print(next_smaller(135))
    return

if __name__ == "__main__":
    main()
