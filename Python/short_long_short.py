#   Sum by Factors - CodeWars
#   Nilton Gomes Martins Junior
#   14/11/2018
#   https://www.codewars.com/kata/short-long-short/train/python

def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b

if __name__ == '__main__':
    print(solution('1', '22'))
