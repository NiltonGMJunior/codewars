#   What's a Perfect Power anyway? - CodeWars
#   Nilton Gomes Martins Junior
#   30/08/2018
#   https://www.codewars.com/kata/whats-a-perfect-power-anyway/train/python

'''
# isPP(n) - Function that defines wheter or not an integer n (greater than 1) can be
represented as a perfect power, i. e., m^k = n, where m and k are integers,
with m > 1 and k > 0. If n is a perfect power, return any (m, k) that satisfy
this property. Else, return None.
'''
def isPP(n):

    i = 1
    while True:
        k = 2
        if n % 2 == 0:
            if (2*i)**k > n:
                break
            while True:
                if (2*i)**k == n:
                    return [2*i, k]
                elif (2*i)**k > n:
                    break
                else:
                    k += 1
        else:
            if (2*i + 1)**k > n:
                break
            while True:
                if (2*i + 1)**k == n:
                    return [2*i + 1, k]
                elif (2*i + 1)**k > n:
                    break
                else:
                    k += 1
        i += 1

    return None

def main():
    print(isPP(150))
    return

if __name__ == "__main__":
    main()
