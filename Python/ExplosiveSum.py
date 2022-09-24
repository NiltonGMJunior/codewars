#   Explosive Sum   -   CodeWars
#   Nilton Gomes Martins Junior
#   02/09/2018
#   https://www.codewars.com/kata/52ec24228a515e620b0005ef/train/python

def count_partitions(n):
    

def cached_exec(cache, n):
    if n not in cache:
        result = count_partitions(n)
    return result

def exp_sum(n):
    cache = {1: 1}
    cache[n] = cached_exec(cache, n)
    return cache[n]

def main():

    return

if __name__ == "__main__":
    main()
