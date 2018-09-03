#   Magnet particules in boxes   -   CodeWars
#   Nilton Gomes Martins Junior
#   02/09/2018
#   https://www.codewars.com/kata/magnet-particules-in-boxes/train/python

# TODO: Algorithm works for some indices but maximum recursion error occurs for large inputs

def v(k, n):
    return 1 / (k * (n + 1) ** (2 * k))

def u(k, n):
    if n == 1:
        return v(k, n)
    else:
        return v(k, n) + u(k, n - 1)

def doubles(maxk, maxn):
    if maxk == 1:
        return u(maxk, maxn)
    else:
        return u(maxk, maxn) + doubles(maxk - 1, maxn)

def main():
    print(doubles(20, 10000))
    return

if __name__ == "__main__":
    main()
