from aoc.puzzle import Part1
import re

cols = 101
rows = 103
seconds = 100

class AocPuzzle(Part1):
    def solve(self, input_str: str):
        map = [['.' for _ in range(cols)] for _ in range(rows)]

        def parse(robot):
            match = re.fullmatch(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', robot)
            p_x, p_y = int(match.group(2)), int(match.group(1))
            v_x, v_y = int(match.group(4)), int(match.group(3))
            return ((p_x, p_y), (v_x, v_y))

        robots = list(zip(*[parse(robot.strip()) for robot in input_str.strip().splitlines()]))
        r_p = list(robots[0])
        r_v = list(robots[1])
        for (x, y) in r_p:
            if map[x][y] == '.':
                map[x][y] = '1'
            else:
                map[x][y] = str(int(map[x][y]) + 1)

        for i in range(len(r_p)):
            p_x_i, p_y_i = r_p[i]
            v_x_i, v_y_i = r_v[i]

            curr_val = int(map[p_x_i][p_y_i]) - 1
            if curr_val > 0:
                map[p_x_i][p_y_i] = str(curr_val)
            else:
                map[p_x_i][p_y_i] = '.'

            new_p_x, new_p_y = (p_x_i + v_x_i * seconds) % rows, (p_y_i + v_y_i * seconds) % cols

            if map[new_p_x][new_p_y] == '.':
                map[new_p_x][new_p_y] = '1'
            else:
                map[new_p_x][new_p_y] = str(int(map[new_p_x][new_p_y]) + 1)

        def count_quadrant(x_start, x_end, y_start, y_end):
            sum = 0
            for x in range(x_start, x_end):
                for y in range(y_start, y_end):
                    if map[x][y] != '.':
                        sum += int(map[x][y])
            return sum

        middle_row = rows // 2
        middle_col = cols // 2

        quadrants = [((0, middle_row), (0, middle_col)),
                     ((middle_row + 1, rows), (0, middle_col)),
                     ((0, middle_row), (middle_col + 1, cols)),
                     ((middle_row + 1, rows), (middle_col + 1, cols))]

        total = 1
        for (x_start, x_end), (y_start, y_end) in quadrants:
            total = total * count_quadrant(x_start, x_end, y_start, y_end)

        return total

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 14)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 225552000 == answer
