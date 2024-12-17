from aoc.puzzle import Part2

BOX = 'O'
FLOOR = '.'
ROBOT = '@'
WALL = '#'
dir = {'>': 1, '<': -1, '^': -1, 'v': 1}

class AocPuzzle(Part2):
    def solve(self, input_str: str):
        warehouse, movements = input_str.split('\n\n')
        warehouse, robot = [
            [('[' if i % 2 == 0 else ']') if line[i // 2] == BOX else line[i // 2] for i in range(len(line) * 2)] for
            line in warehouse.split()], warehouse.index(ROBOT)
        x, y = robot % (len(warehouse[0]) // 2), robot // (len(warehouse[0]) // 2)

        warehouse[y][x], warehouse[y][x + 1] = FLOOR, FLOOR
        for move in ''.join(movements.split()):
            if move in ['>', '<']:
                x1 = x + (dir[move])
                while warehouse[y][x1] in ['[', ']']: x1 += dir[move]
                if warehouse[y][x1] == FLOOR:
                    for x2 in range(x1, x, -dir[move]): warehouse[y][x2] = warehouse[y][x2 - dir[move]]
                    x += dir[move]
            else:
                boxes = [{(x, y)}]
                while boxes[-1]:
                    boxes.append(set())
                    for box in boxes[-2]:
                        if warehouse[box[1] + dir[move]][box[0]] == WALL:
                            break
                        if warehouse[box[1] + dir[move]][box[0]] == '[':
                            boxes[-1] |= {(box[0], box[1] + dir[move]), (box[0] + 1, box[1] + dir[move])}
                        elif warehouse[box[1] + dir[move]][box[0]] == ']':
                            boxes[-1] |= {(box[0], box[1] + dir[move]), (box[0] - 1, box[1] + dir[move])}
                    else:
                        continue
                    break
                else:
                    for row in list(reversed(boxes)):
                        for box in row:
                            warehouse[box[1] + dir[move]][box[0]], warehouse[box[1]][box[0]] = warehouse[box[1]][box[0]], FLOOR
                    y += dir[move]

        return sum(100 * i + j for i, row in enumerate(warehouse) for j, col in enumerate(row) if col == '[')

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 15)

#     example_input = '''
# ##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########
#
# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
#     '''

    # assert 9021 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 1404917 == answer
