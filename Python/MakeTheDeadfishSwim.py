#   Make the Dead Fish Swim   -   CodeWars
#   Nilton Gomes Martins Junior
#   04/09/2018
#   http://www.codewars.com/kata/make-the-deadfish-swim?utm_source=newsletter

def parse(data):
    output = []
    initial = 0
    for char in data:
        if char == 'i':
            initial += 1
        elif char == 'd':
            initial -= 1
        elif char == 's':
            initial *= initial
        elif char == 'o':
            output.append(initial)
        else:
            pass

    return output

def main():
    print(parse('ooo'))
    return

if __name__ == "__main__":
    main()
