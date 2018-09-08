#   Decypher This - CodeWars
#   Nilton Gomes Martins Junior
#   06/09/2018
#   https://www.codewars.com/kata/decipher-this/train/python

#   TODO:   decypher_word ot working properly

def decypher_word(word):
    numbers = [str(n) for n in range(10)]
    first_char = chr(int(''.join([char for char in word if char in numbers])))
    try:
        remaining = word[len(str(ord(first_char))):]
    except IndexError:
        return first_char

    if len(remaining) == 1:
        return first_char + remaining
    elif len(remaining) == 2:
        return first_char + remaining[::-1]
    else:
        return first_char + remaining[-1] + remaining[1:-1] + remaining[0]

def decipher_this(string):
    return ' '.join([decypher_word(word) for word in string.split()])

def main():
    print(decipher_this("65"))
    return

if __name__ == "__main__":
    main()
