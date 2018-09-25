#   Nilton Gomes Martins Junior
#   26/07/2018
#   Code Wars - Anagram Detection - https://www.codewars.com/kata/anagram-detection

#   Anagrams are case INSENSITIVE

def is_anagram(test, original):
    test, original = list(test.lower()), list(original.lower())
    for index, char in enumerate(test):
        if char in original:
            del test[index]
            del original[original.index(char)]
        else:
            return False
    
    return not(test or original)


def main():
    
    return

if __name__ == "__main__":
    main()