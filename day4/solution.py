def check(x, y, move_x, move_y, matrix):
    to_find = 'XMAS'
    for i in range(len(to_find)):
        next_x = x + i * move_x
        next_y = y + i * move_y

        if (next_x < 0
                or next_x >= len(matrix)
                or next_y < 0
                or next_y >= len(matrix[0])
                or matrix[next_x][next_y] != to_find[i]):
            return False
    return True

def count(matrix):
    move_options = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    total = 0

    for row in range(len(matrix)):
        for character in range(len(matrix[row])):
            for move in move_options:
                if check(row, character, move[0], move[1], matrix):
                    total += 1

    return total

if __name__ == '__main__':
    matrix = []
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            matrix.append(list(line.strip()))
    print(count(matrix))

