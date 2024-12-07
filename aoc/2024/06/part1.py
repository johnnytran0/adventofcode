from setuptools.namespaces import flatten
from aoc.puzzle import Part1
import pprint

obstacle = '#'
visited = 'X'

def rotate_ccw_90(matrix, coords):
    """
    rotates the matrix 90 degrees clockwise and transfer coordinates to rotated matrix.
    Does not reorient guard direction.
    :param matrix: 2d array
    :param coords: a pair of coordinates to transfer
    :return: rotated 2d array and transferred coordinates
    """
    (x, y)  = coords
    rotated_coords = (len(matrix) - 1 - y, x)
    rotated_matrix = [list(col) for col in zip(*matrix)][::-1]

    return rotated_matrix, rotated_coords

def patrol(map, coords):
    """
    Lab guards follow protocol:
    - If there is something directly in front of you, turn right 90 degrees.
    - Otherwise, take a step forward.

    :param map: requires that guard must always be moving to the right, >
    :return: visited map and final patrol coordinates, None if out of bounds?
    """
    (x, y) = coords

    if 0 <= x-1 and map[x-1][y] == obstacle:
        # turn right 90 degrees
        return rotate_ccw_90(map, coords)
    else:
        # mark current node as visited
        guard = map[x][y]
        map[x][y] = visited
        if 0 <= x-1:
            # take step
            map[x-1][y] = guard
            return map, (x-1, y)
        else:
            return map, None

class PuzzlePart1(Part1):
    def solve(self, input_str: str):
        """
        assumes initial guard direction is up, ^
        :param input_str:
        :return:
        """
        map = [[z for z in row.strip()] for row in input_str.strip().splitlines()]
        rows, cols = len(map), len(map[0])
        pprint.pprint(map)
        print(f'rows: {rows}, cols: {cols}')

        # find initial position of guard
        guard_coords = next((x, y) for x in range(rows) for y in range(cols) if map[x][y] == '^')

        rotated_map, rotated_coords = map, guard_coords

        while rotated_coords:
            rotated_map, rotated_coords = patrol(rotated_map, rotated_coords)

        return sum(1 for x in flatten(rotated_map) if x == visited)

if __name__ == '__main__':
    puzzle = PuzzlePart1(2024, 6)

    example_input = '''
        ....#.....
        .........#
        ..........
        ..#.......
        .......#..
        ..........
        .#..^.....
        ........#.
        #.........
        ......#...
        '''

    assert 41 == puzzle.solve(example_input)

    example_answer = puzzle.solve(puzzle.input())
    print(f'answer: {example_answer}')
    assert 4939 == example_answer
