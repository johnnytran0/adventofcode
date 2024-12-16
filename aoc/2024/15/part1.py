from aoc.puzzle import Part1
from pprint import pprint

BOX = 'O'
FLOOR = '.'
ROBOT = '@'
WALL = '#'
dir = {'^': (-1, 0), '>': (0, 1), "v": (1,0), "<": (0, -1)}

class AocPuzzle(Part1):
    def solve(self, input_str: str):
        warehouse, movements = input_str.strip().split('\n\n')
        warehouse = [[foo for foo in bar] for bar in warehouse.splitlines()]
        pprint(warehouse)

        movements = movements.replace('\n', '')

        print(f'movements = {len(movements)}')
        rows = len(warehouse)
        cols = len(warehouse[0])
        r_x = r_y = 0

        # find robot initial position
        for row in range(rows):
            for col in range(cols):
                if warehouse[row][col] == ROBOT:
                    r_y = row
                    r_x = col
                    break

        def cascade_boxes(box_x, box_y, dx, dy):
            next_x = box_x + dx
            next_y = box_y + dy

            if 0 < next_x < cols - 1 and 0 < next_y < rows - 1:
                if warehouse[next_x][next_y] == FLOOR:
                    warehouse[next_x][next_y] = BOX
                    warehouse[box_x][box_y] = FLOOR
                elif warehouse[next_x][next_y] == BOX:
                    print(f'cascading box at {next_x, next_y}')
                    cascade_boxes(next_x, next_y, dx, dy)
                    if warehouse[next_x][next_y] == FLOOR:
                        warehouse[next_x][next_y] = BOX
                        warehouse[box_x][box_y] = FLOOR

        def robot(r_x, r_y, move):
            dx, dy = dir[move]
            print(f'starting at {r_x,r_y}, moving {move}')
            new_y = r_y + dy
            new_x = r_x + dx

            if warehouse[new_x][new_y] != WALL:
                if warehouse[new_x][new_y] == BOX:
                    cascade_boxes(new_x, new_y, dx, dy)
                    if 0 < new_x < cols - 1 and 0 < new_y < rows - 1 and warehouse[new_x][new_y] == FLOOR:
                            warehouse[new_x][new_y] = ROBOT
                            warehouse[r_x][r_y] = FLOOR
                            return new_x, new_y
                    return r_x, r_y
                else:
                    warehouse[new_x][new_y] = ROBOT
                    warehouse[r_x][r_y] = FLOOR
                return new_x, new_y
            else:
                # found wall, stay in place
                return r_x, r_y

        for move in movements:
            r_x, r_y = robot(r_x, r_y, move)
            # pprint(warehouse)


        return sum(100 * row + col for row in range(rows) for col in range(cols) if warehouse[row][col] == BOX)

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 15)

    example_input = '''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
    '''

    assert 2028 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 1426855 == answer
