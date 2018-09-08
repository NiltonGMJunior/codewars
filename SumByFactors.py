#   Sum by Factors - CodeWars
#   Nilton Gomes Martins Junior
#   08/09/2018
#   https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python

#   TODO:   Implement a function that filters only prime elements among the divisors of the lst elements
#   TODO:   Implement the sum_for_list function that solves the initial problem

def get_divisors(cache, n):
    for k in range(2, n//2 + 1):
        if n % k == 0 and k not in cache[n]:
            cache[n].append(k)
            if k in cache:
                for elem in cache[k]:
                    if elem not in cache[n]:
                        cache[n].append(elem)

    return cache, divisors

def cached_exec(cache, n):
    if n not in cache:
        cache[n] = get_divisors(n)
    return cache, cache[n]

def sum_for_list(lst):
    cache = {}
    return

def main():)
    return

if __name__ == "__main__":
    main()
