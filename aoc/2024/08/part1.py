from aoc.puzzle import Part1
from collections import defaultdict
from pprint import pprint
import re

class PuzzlePart1(Part1):
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
                    print(f'{freq} at {x,y}')
                    antenna_map[freq].append([x,y])

        antinodes = [[False for _ in range(cols)] for _ in range(rows)]

        for freq, antennas in antenna_map.items():
            for i in range(len(antennas)-1):
                for j in range(i+1, len(antennas)):
                    x_diff = antennas[i][0] - antennas[j][0]
                    y_diff = antennas[i][1] - antennas[j][1]

                    antinode_i_x, antinode_i_y = antennas[i][0] + x_diff, antennas[i][1] + y_diff
                    if 0 <= antinode_i_x < rows and 0 <= antinode_i_y < cols:
                        antinodes[antinode_i_x][antinode_i_y] = True

                    antinode_j_x, antinode_j_y = antennas[j][0] - x_diff, antennas[j][1] - y_diff
                    if 0 <= antinode_j_x < rows and 0 <= antinode_j_y < cols:
                        antinodes[antinode_j_x][antinode_j_y] = True

        pprint(antinodes)

        return sum(sum(1 for val in col if val) for col in antinodes)

if __name__ == '__main__':
    puzzle = PuzzlePart1(2024, 8)

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

    assert 14 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 261 == answer
