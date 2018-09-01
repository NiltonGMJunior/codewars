#   Gap in Primes - CodeWars
#   Nilton Gomes Martins Junior
#   30/08/2018
#   https://www.codewars.com/kata/gap-in-primes/train/python

def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime(n):
    return prime(n + 1) if not isPrime(n) else n

def gap(g, m, n):

    base = m

    while True:
        first_prime = prime(base) # Finds the first prime greater than or equal to base
        second_prime = prime(first_prime + 1) # Finds the first prime greater than or equal to first_prime + 1
        if first_prime > n or second_prime > n:
            break
        if second_prime - first_prime == g:
            return [first_prime, second_prime]
        else:
            base = second_prime
    return None

def main():
    print(gap(6, 100, 110))
    return

if __name__ == "__main__":
    main()
