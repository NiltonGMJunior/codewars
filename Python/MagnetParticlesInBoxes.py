#   Bubblesort Once   -   CodeWars
#   Nilton Gomes Martins Junior
#   04/09/2018
#   http://www.codewars.com/kata/bubblesort-once/train/python

def bubblesort_once(l):
    for index, elem in enumerate(l[1:]):
        if elem < l[index - 1]:
            l[index - 1], l[index] = elem, l[index - 1]
    return l

def main():
    print(bubblesort_once([3,1,2]))
    return

if __name__ == "__main__":
    main()
