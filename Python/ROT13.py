#   Sum by Factors - CodeWars
#   Nilton Gomes Martins Junior
#   14/11/2018
#   https://www.codewars.com/kata/rot13/train/python

def decypher_char_rot13(char):
    char_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    if char in char_list:
        #   Decypher as lower case char then return as lower case
        if ord(char) + 13 <= ord('z'):
            return chr(ord(char) + 13)
        else:
            return chr(ord('a') + (ord(char) + 13) % ord('z') - 1)
    elif char.lower() in char_list:
        #   Decypher as lower case char then return as upper case
        return decypher_char_rot13(char.lower()).upper()
    else:
        return char

def rot13(message):

    encrypted_words = message.split()
    words = []

    for word in encrypted_words:
        words.append(''.join([decypher_char_rot13(char) for char in word]))

    return ' '.join(words)

if __name__ == '__main__':
    # print(decypher_char_rot13('m'))
    print(rot13('EBG13 rknzcyr.'))
    print(rot13("This is my first ROT13 excercise!"))
