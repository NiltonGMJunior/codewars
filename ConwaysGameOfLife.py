#   Conway's Game of Life - Unlimited Edition   -   CodeWars
#   Nilton Gomes Martins Junior
#   31/08/2018
#   https://www.codewars.com/kata/52423db9add6f6fc39000354/train/python
def remove_zeros_up(cells):

    test_row = cells[0]
    if any(test_row):
        return cells

    return remove_zeros_up(cells[1:])

def remove_zeros_down(cells):

    test_row = cells[-1]
    if any(test_row):
        return cells

    return remove_zeros_down(cells[:-1])

def remove_zeros_left(cells):

    test_column = [row[0] for row in cells]
    if any(test_column):
        return cells

    return remove_zeros_left([row[1:] for row in cells])

def remove_zeros_right(cells):

    test_column = [row[-1] for row in cells]
    if any(test_column):
        return cells

    return remove_zeros_right([row[:-1] for row in cells])

def append_zeros_frame(cells):

    new_cells = [[elem for elem in row] for row in cells]
    new_cells = [[0] + row + [0] for row in new_cells]
    new_length = len(new_cells[0])

    return [[0]*new_length] + new_cells + [[0]*new_length]

def remove_zeros_frame(cells):

    new_cells = [[elem for elem in row] for row in cells]

    new_cells = remove_zeros_up(new_cells)
    new_cells = remove_zeros_down(new_cells)
    new_cells = remove_zeros_left(new_cells)
    new_cells = remove_zeros_right(new_cells)

    return new_cells

def new_state(cells, i, j):

    initial_state = 'Live' if cells[i][j] == 1 else 'Dead'
    count_live_cells = 0

    for m in [-1, 0, 1]:
        for n in [-1, 0, 1]:
            if all([not(m == 0 and n == 0), i + m >= 0, j + n >= 0]):
                try:
                    count_live_cells += cells[i + m][j + n] == 1
                except IndexError:
                    continue

    if initial_state == 'Live':
        return 1 if count_live_cells in [2, 3] else 0
    else:
        return 1 if count_live_cells == 3 else 0

def get_generation(cells, generations):
    if generations == 0:
        return remove_zeros_frame(cells)
    else:
        reference = [[elem for elem in row] for row in cells]
        reference = append_zeros_frame(reference)

        new_cells = [[elem for elem in row] for row in cells]
        new_cells = append_zeros_frame(new_cells)
        for i in range(len(new_cells)):
            for j in range(len(new_cells[i])):
                new_cells[i][j] = new_state(reference, i, j)
    return get_generation(new_cells, generations - 1)

def main():
    start = [[1,0,0], [0,1,1], [1,1,0]]
    print(get_generation(start, 1))
    # test = [[0, 0, 0], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0]]
    # print(remove_zeros_right(test))
    return

if __name__ == "__main__":
    main()
