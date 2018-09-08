#   Encrypt This - CodeWars
#   Nilton Gomes Martins Junior
#   06/09/2018
#   https://www.codewars.com/kata/encrypt-this

def encrypt_this_word(text):
    output = str(ord(text[0]))
    if len(text) > 1:
        try:
            output += text[-1]
            output += text[2:-1]
            output += text[1] if len(text) >= 3 else ''
        except IndexError:
            pass

    return output

def encrypt_this(text):
    words = [word for word in text.split()]
    return ' '.join([encrypt_this_word(word) for word in words])

def main():
    print(encrypt_this('Hello'))
    return

if __name__ == "__main__":
    main()
