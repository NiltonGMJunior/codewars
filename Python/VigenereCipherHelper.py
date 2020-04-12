#   Vigenère Cipher Helper
#   Nilton Gomes Martins Junior
#   11/04/2020
#   https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        normalized_key = (self.key * (len(text) // len(self.key) + 1))[:len(text)]
        encoded_text = ""
        for index, char in enumerate(text):
            if char in self.alphabet:
                encoded_text += rotate_chars(self.alphabet, char, self.alphabet.index(normalized_key[index]))
            else:
                encoded_text += char
        return encoded_text

    def decode(self, text):
        normalized_key = (self.key * (len(text) // len(self.key) + 1))[:len(text)]
        decoded_text = ""
        for index, char in enumerate(text):
            if char in self.alphabet:
                decoded_text += rotate_chars(self.alphabet, char, -self.alphabet.index(normalized_key[index]))
            else:
                decoded_text += char
        return decoded_text

def rotate_chars(alphabet, initial_char, shifted_chars):
    if alphabet.index(initial_char) == -1:
        return None

    alphabet_size = len(alphabet)
    initial_char_index = alphabet.index(initial_char)
    if (shifted_chars >= 0):
        initial_char_index = alphabet.index(initial_char)     
        return alphabet[(initial_char_index + shifted_chars) % alphabet_size]
    else:
        return alphabet[(alphabet_size + initial_char_index + shifted_chars) % alphabet_size] 

if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = VigenereCipher("password", alphabet)
    print(cipher.encode("codewars"))
    print(cipher.decode("rovwsoiv"))