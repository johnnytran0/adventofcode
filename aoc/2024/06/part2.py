from aoc.puzzle import Part2
from copy import deepcopy
import multiprocessing
import time

# clockwise order
directions = ('north', 'east', 'south', 'west')
obstacle = '#'
visited = 'X'

def rotate_ccw_90(matrix, coords, orientation):
    """
    rotates the matrix 90 degrees counterclockwise and transfer coordinates to rotated matrix.
    does not rotate the orientation of the guard so guard's perspective turns to the right
    :param matrix: 2d array
    :param coords: a pair of coordinates to transfer
    :return: rotated 2d array and transferred coordinates
    """
    (x, y)  = coords
    rotated_coords = (len(matrix) - 1 - y, x)
    rotated_matrix = [list(col) for col in zip(*matrix)][::-1]
    rotated_orientation = directions[(directions.index(orientation) + 1) % 4]
    return rotated_matrix, rotated_coords, rotated_orientation

def patrol(map, coords, orientation):
    """
    Lab guards follow protocol:
    - If there is something directly in front of you, turn right 90 degrees.
    - Otherwise, take a step forward.
    :param map: requires that guard must always be moving to the right, >
    :return: visited map and final patrol coordinates, None if out of bounds?
    """
    (x, y) = coords

    if 0 <= x-1 and map[x-1][y][0] == obstacle:
        if map[x-1][y][0] == obstacle:
            # check if obstacle has been visited from this direction
            guard_orientation = orientation
            if guard_orientation in map[x-1][y][1]:
                # found loop because obstacle has already been visited from this orientation
                return None, None, None, True
            else:
                # indicates obstacle has been visited from this orientation
                map[x - 1][y][1].add(guard_orientation)
        # turn guard right 90 degrees
        return rotate_ccw_90(map, coords, orientation), False
    else:
        # mark current node as visited
        guard = map[x][y][0]
        map[x][y] = (visited, None)
        if 0 <= x-1:
            # take a step forward
            map[x-1][y] = (guard, None)
            return map, (x-1, y), orientation, False
        else:
            # guard has left the boundaries of map
            return map, None, orientation, False

class PuzzlePart2(Part2):
    def find_loop(self, obstruction_coords):
        # create obstruction map to track visits
        obstructed_map = deepcopy(self.map)
        obstructed_map[obstruction_coords[0]][obstruction_coords[1]] = obstacle

        # replaces map cell with a tuple for tracking visits to an obstacle
        visited_map = [[(val, set() if val == obstacle else None) for val in rows] for rows in obstructed_map]
        coords = self.guard_coords
        orientation = directions[0]
        while coords:
            visited_map, coords, orientation, has_loop = patrol(visited_map, coords, orientation)
            if has_loop:
                return True
        return False

    def solve(self, input_str: str):
        """
        assumes initial guard direction is up, ^
        :param input_str:
        :return:
        """
        self.map = [[val for val in row.strip()] for row in input_str.strip().splitlines()]
        rows, cols = len(self.map), len(self.map[0])

        self.guard_coords = next((x, y) for x in range(rows) for y in range(cols) if self.map[x][y] == '^')

        obstruction_coords = [(x, y) for x in range(rows) for y in range(cols) if self.map[x][y] == '.']

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            # call the same function with different data in parallel
            return sum(pool.map(self.find_loop, obstruction_coords))

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

    start = time.time()
    answer = puzzle.solve(puzzle.input())
    print(f'completed in {time.time() - start} seconds')

    print(f'answer: {answer}')
    assert 1434 == answer
