#   The Hunger Games - Zoo Disaster!   -   CodeWars
#   Nilton Gomes Martins Junior
#   31/08/2018
#   https://www.codewars.com/kata/5902bc7aba39542b4a00003d/train/python

# TODO: Code still doens't satisfy all test conditions

FOOD_CHAIN = {'antelope':['grass'], 'big-fish':['little-fish'], 'bug':['leaves'], 'bear':['bug', 'chicken', 'cow', 'leaves', 'sheep'], 'chicken':['bug'], 'cow':['grass'], 'fox':['chicken', 'sheep'], 'giraffe':['leaves'], 'lion':['antelope', 'cow'], 'panda':['leaves'], 'sheep':['grass']}

def who_eats_who(zoo):
    animals = zoo.split(',')
    feeding = []
    while True:
        changes = 0
        for (index, animal) in enumerate(animals):
            try:
                if animals[index - 1] in FOOD_CHAIN[animal] and index -1 >= 0:
                    feeding.append(animal + ' eats ' + animals[index - 1])
                    del animals[index - 1]
                    changes += 1
                    break
                elif animals[index + 1] in FOOD_CHAIN[animal]:
                    feeding.append(animal + ' eats ' + animals[index + 1])
                    del animals[index + 1]
                    changes += 1
                    break
            except IndexError:
                pass
            except KeyError:
                pass
        if changes == 0:
            break

    new_zoo = ','.join(animals)

    return [zoo] + feeding + [new_zoo]

def main():
    zoo = "fox,bug,chicken,grass,sheep"
    # print(list(enumerate(zoo.split(','))))
    print(who_eats_who(zoo))
    return

if __name__ == "__main__":
    main()
