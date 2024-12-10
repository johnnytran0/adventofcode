from aoc.puzzle import Part2
from copy import copy

trailhead_symbol = 0
target_symbol = 9

class AocPuzzle(Part2):
    def solve(self, input_str: str):
        topo = [[int(y) for y in x.strip()] for x in input_str.strip().splitlines() if x]
        rows, cols = len(topo), len(topo[0])

        def count_paths(trailhead):
            paths = []

            # return unique paths starting from trailhead
            def search(stack, visited):
                if stack:
                    x, y = stack.pop(0)
                    visited.append((x,y))
                    curr_height = topo[x][y]
                    if curr_height == target_symbol:
                        paths.append(visited)
                    else:
                        for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            new_x, new_y = x + xx, y + yy
                            next_position = (new_x, new_y)
                            if 0<=new_x<rows and 0<=new_y<cols and next_position not in visited:
                                next_height = topo[new_x][new_y]
                                if curr_height + 1 == next_height:
                                    search(stack + [next_position], copy(visited))

            search([trailhead], [])
            return len(paths)

        trailheads = [(x,y) for x in range(len(topo)) for y in range(len(topo[0])) if topo[x][y] == trailhead_symbol]

        # unique paths to all reachable 9-height positions per trailhead
        return sum([count_paths(trailhead) for trailhead in trailheads])

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 10)

    example_input = '''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
        '''

    assert 81 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 1511 == answer
