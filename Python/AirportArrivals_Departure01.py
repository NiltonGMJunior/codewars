#   Airport Arrivals/Departures - #1   -   CodeWars
#   Nilton Gomes Martins Junior
#   02/09/2018
#   https://www.codewars.com/kata/57feb00f08d102352400026e/train/python

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'

def change_char(char, turns):
    return ALPHABET[(ALPHABET.index(char) + turns) % len(ALPHABET)]

def change_line(line, rotor):
    output = [char for char in line] # Deep copies line to avoid changing it during the transformation
    for index, char in enumerate(line):
        for k in range(index, len(line)):
            output[k] = change_char(output[k], rotor[index])
    return ''.join(output)

def flap_display(lines, rotors):
    output = []
    for index, line in enumerate(lines):
        # Changes line according to the appropriate rotor input and appends the result to the output list
        output.append(change_line(line, rotors[index]))
    return output

def main():
    print(flap_display(['CAT'],[[1, 13, 27]]))
    # print(change_char('A', 54))
    return

if __name__ == "__main__":
    main()
