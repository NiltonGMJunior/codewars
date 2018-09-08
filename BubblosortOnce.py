#   Bubblesort Once   -   CodeWars
#   Nilton Gomes Martins Junior
#   04/09/2018
#   http://www.codewars.com/kata/bubblesort-once/train/python

def bubblesort_once(l):
    sorted_list = l[:]
    for k in range(len(sorted_list) - 1):
        if sorted_list[k] > sorted_list[k + 1]:
            sorted_list[k], sorted_list[k + 1] = sorted_list[k + 1], sorted_list[k]
    return sorted_list

def main():
    print(bubblesort_once([3,1,2]))
    return

if __name__ == "__main__":
    main()
