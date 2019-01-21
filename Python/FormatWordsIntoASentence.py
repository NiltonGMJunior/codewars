#   Sum by Factors - CodeWars
#   Nilton Gomes Martins Junior
#   14/11/2018
#   https://www.codewars.com/kata/format-words-into-a-sentence/train/python

def format_words(words):
    if words == None:
        return ''

    words = [word for word in words if word]

    if len(words) == 0:
        return ''
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return ' and '.join(words)
    else:
        return ', '.join(words[:-1]) + ' and ' + words[-1]

if __name__ == '__main__':
    print(format_words(['one', '', '', 'two', 'three', 'four']))
    print(format_words(None))
