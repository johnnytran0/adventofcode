from aoc.puzzle import Part2
from collections import defaultdict
from pprint import pprint
import re

class PuzzlePart2(Part2):
    def solve(self, input_str: str):
        map = [[val for val in line.strip()] for line in input_str.strip().splitlines()]
        rows, cols = len(map), len(map[0])
        print(f'{rows, cols}')
        pprint(map)

        antenna_map = defaultdict(list)

        for x in range(rows):
            for y in range(cols):
                if re.match(r'[a-zA-Z0-9]', map[x][y]):
                    freq = map[x][y]
                    print(f'{freq} at {x, y}')
                    antenna_map[freq].append([x, y])

        antinodes = [['.' for _ in range(cols)] for _ in range(rows)]

        for freq, antennas in antenna_map.items():

            if len(antennas) > 1:
                for a in antennas:
                    antinodes[a[0]][a[1]] = '#'

            for i in range(len(antennas) - 1):
                a_i = antennas[i]

                for j in range(i + 1, len(antennas)):
                    a_j = antennas[j]

                    x_diff = a_i[0] - a_j[0]
                    y_diff = a_i[1] - a_j[1]

                    antinode_i_x, antinode_i_y = a_i[0] + x_diff, a_i[1] + y_diff
                    while 0 <= antinode_i_x < rows and 0 <= antinode_i_y < cols:
                        antinodes[antinode_i_x][antinode_i_y] = '#'
                        antinode_i_x, antinode_i_y = antinode_i_x + x_diff, antinode_i_y + y_diff

                    antinode_j_x, antinode_j_y = a_j[0] - x_diff, a_j[1] - y_diff
                    while 0 <= antinode_j_x < rows and 0 <= antinode_j_y < cols:
                        antinodes[antinode_j_x][antinode_j_y] = '#'
                        antinode_j_x, antinode_j_y = antinode_j_x - x_diff, antinode_j_y - y_diff

        pprint(antinodes)

        return sum(sum(1 for val in col if val == '#') for col in antinodes)

if __name__ == '__main__':
    puzzle = PuzzlePart2(2024, 8)

    example_input = '''
        ............
        ........0...
        .....0......
        .......0....
        ....0.......
        ......A.....
        ............
        ............
        ........A...
        .........A..
        ............
        ............
        '''

    assert 34 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 898 == answer
