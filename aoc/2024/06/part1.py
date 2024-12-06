from setuptools.namespaces import flatten
from aoc.puzzle import Part1
import pprint

# clockwise rotation: up, right, down, left, ...
guards = ('^', '>', 'v', '<')
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

def rotate_cw_90(matrix, coords):
    """
    rotates the matrix 90 degrees clockwise and transfer coordinates to rotated matrix.
    Does not reorient guard direction.
    :param matrix: 2d array
    :param coords: a pair of coordinates to transfer
    :return: rotated 2d array and transferred coordinates
    """
    (x, y)  = coords
    rotated_coords = (y, len(matrix) - 1 - x)
    rotated_matrix = [list(col)[::-1] for col in zip(*matrix)]

    return rotated_matrix, rotated_coords

def reorient_map(map, coords):
    ## reorient map
    rotated_map, rotated_coords = rotate_cw_90(map, coords)

    # reorient guard direction CCW, so that guard is always travelling to the right through the columns
    next_guard_dir_index = (guards.index(rotated_map[rotated_coords[0]][rotated_coords[1]]) + 1) % 4
    rotated_map[rotated_coords[0]][rotated_coords[1]] = guards[next_guard_dir_index]

    return rotated_map, rotated_coords

def patrol(map, coords):
    """
    Lab guards follow protocol:
    - If there is something directly in front of you, turn right 90 degrees.
    - Otherwise, take a step forward.

    :param map: requires that guard must always be moving to the right, >
    :return: visited map and final patrol coordinates, None if out of bounds?
    """
    (x, y) = coords

    # guard is out of bounds when i | j < 0 or last_row_i, last_row_J < i | j
    last_col_y = len(map[0])-1

    if y + 1 <= last_col_y and map[x][y+1] == obstacle:
        # turn right 90 degrees
        right_turn_map, right_turn_coords = rotate_ccw_90(map, coords)
        return right_turn_map, right_turn_coords
    else:
        # mark current node as visited
        guard = map[x][y]
        map[x][y] = visited
        if y + 1 <= last_col_y:
            # take step
            map[x][y+1] = guard
            return map, (x, y+1)
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
        # pprint.pprint(map)
        # rows, cols = len(map), len(map[0])
        # print(f'rows: {rows}, cols: {cols}')

        guard_x, guard_y = 0, 0
        for i, row in enumerate(map):
            for j, cell in enumerate(row):
                if cell in guards:
                    guard_x, guard_y = i, j
                    # print(f'found guard: {guard_x, guard_y}, {map[guard_x][guard_y]}')
                    break

        rotated_map, rotated_coords = reorient_map(map, (guard_x, guard_y))

        while rotated_coords:
            rotated_map, rotated_coords = patrol(rotated_map, rotated_coords)

        pprint.pprint(rotated_map)

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
