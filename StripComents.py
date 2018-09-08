#   Strip Comments - CodeWars
#   Nilton Gomes Martins Junior
#   08/09/2018
#   https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def remove_trailing_whitespace(line):
    try:
        return line if line[-1] != ' ' else remove_trailing_whitespace(line[:-1])
    except IndexError:
        return line

def solution(string, markers):
    lines = string.split('\n')
    for marker in markers:
        for index, line in enumerate(lines):
            lines[index] = line.split(marker)[0]
    return '\n'.join([remove_trailing_whitespace(line) for line in lines])

def main():
    print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
    return

if __name__ == "__main__":
    main()
