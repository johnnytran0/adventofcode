from aoc.puzzle import Part2
from copy import deepcopy
import pprint

# clockwise rotation: up, right, down, left, ...
guards = ('^', '>', 'v', '<')
direction = ('north', 'east', 'south', 'west')
obstacle = '#'
visited = 'X'

def rotate_ccw_90(matrix, coords, orientation):
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
    rotated_orientation = direction[(direction.index(orientation) + 1) % 4]
    return rotated_matrix, rotated_coords, rotated_orientation

def rotate_cw_90(matrix, coords, orientation):
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
    rotated_orientation = direction[(direction.index(orientation) - 1) % 4]
    return rotated_matrix, rotated_coords, rotated_orientation

def reorient_map(map, coords, orientation):
    ## reorient map
    rotated_map, rotated_coords, rotated_orientation = rotate_cw_90(map, coords, orientation)

    # reorient guard direction CCW, so that guard is always travelling to the right through the columns
    next_guard_dir_index = (guards.index(rotated_map[rotated_coords[0]][rotated_coords[1]][0]) + 1) % 4
    rotated_map[rotated_coords[0]][rotated_coords[1]] = (guards[next_guard_dir_index], rotated_map[rotated_coords[0]][rotated_coords[1]][1])

    return rotated_map, rotated_coords, rotated_orientation

def patrol(map, coords, orientation):
    """
    Lab guards follow protocol:
    - If there is something directly in front of you, turn right 90 degrees.
    - Otherwise, take a step forward.

    :param map: requires that guard must always be moving to the right, >
    :return: visited map and final patrol coordinates, None if out of bounds?
    """
    (x, y) = coords

    last_col_y = len(map[0])-1

    if y + 1 <= last_col_y and map[x][y+1][0] == obstacle:
        if map[x][y+1][0] == obstacle:
            # check if obstacle has been visited from this direction
            guard_orientation = direction[(direction.index(orientation) + 1) % 4]
            if guard_orientation in map[x][y+1][1]:
                # found loop because obstacle has already been visited from this orientation
                return None, None, None, True
            else:
                # indicates obstacle has been visited from this orientation
                map[x][y+1][1].add(guard_orientation)
        # turn guard right 90 degrees
        right_turn_map, right_turn_coords, right_turn_orientation= rotate_ccw_90(map, coords, orientation)
        return right_turn_map, right_turn_coords, right_turn_orientation, False
    else:
        # mark current node as visited
        guard = map[x][y][0]
        map[x][y] = (visited, None)
        if y + 1 <= last_col_y:
            # take next step to the right
            map[x][y+1] = (guard, None)
            return map, (x, y+1), orientation, False
        else:
            # guard has left the boundaries of map
            return map, None, orientation, False

def find_loop(map, coords, orientation):
    rotated_map, rotated_coords, rotated_orientation = reorient_map(map, coords, orientation)
    while rotated_coords:
        rotated_map, rotated_coords, rotated_orientation, has_loop = patrol(rotated_map, rotated_coords, rotated_orientation)
        if has_loop:
            return True
    return False

class PuzzlePart2(Part2):
    def solve(self, input_str: str):
        """
        assumes initial guard direction is up, ^
        :param input_str:
        :return:
        """
        map = [[z for z in row.strip()] for row in input_str.strip().splitlines()]
        # pprint.pprint(map)
        rows, cols = len(map), len(map[0])

        # find initial position of guard
        guard_coords = None
        orientation = direction[0]
        for x in range(rows):
            for y in range(cols):
                if map[x][y] in guards:
                    guard_coords = (x, y)
                    break

        obstructed_loops = 0
        print(f'rows: {rows}, cols: {cols}')
        for row in range(rows):
            for col in range(cols):
                cell = map[row][col]
                if cell == '.':
                    # print(f'{row, col}: {cell} overwritten with obstacle')

                    obstructed_map = deepcopy(map)
                    obstructed_map[row][col] = obstacle

                    visited_map = [[(val, set() if val == obstacle else None) for val in rows] for rows in obstructed_map]
                    if find_loop(visited_map, guard_coords, orientation):
                        print(f'obstruction at {row, col} causes a loop')
                        obstructed_loops += 1
        return obstructed_loops

if __name__ == '__main__':
    puzzle = PuzzlePart2(2024, 6)

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
    assert 6 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 1434 == answer
