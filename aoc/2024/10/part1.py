from aoc.puzzle import Part1
from pprint import pprint

trailhead_symbol = 0
target_symbol = 9
class AocPuzzle(Part1):
    def solve(self, input_str: str):
        topo = [[int(y) for y in x.strip()] for x in input_str.strip().splitlines() if x]
        rows, cols = len(topo), len(topo[0])

        def bfs(stack):
            curr_score = 0

            while stack:
                print(f'exploring with len(stack): {len(stack)}')
                x, y = stack.pop(0)
                curr_height = topo[x][y]
                if curr_height == target_symbol:
                    curr_score += 1
                    print(f'found target, current score is now {curr_score}')
                else:
                    print(f'exploring at {curr_height}')
                    for xx, yy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_x, new_y = x + xx, y + yy
                        next_position = (new_x, new_y)
                        if 0<=new_x<rows and 0<=new_y<cols and next_position not in stack:
                            next_height = topo[new_x][new_y]
                            if curr_height + 1 == next_height:
                                print(f'found gradual adjacent path {x + xx, y + yy} with height {next_height}')
                                stack.append(next_position)
            return curr_score
        pprint(topo)

        trailheads = [(x,y) for x in range(len(topo)) for y in range(len(topo[0])) if topo[x][y] == trailhead_symbol]
        print(trailheads)
        print(f'there are {len(trailheads)} trailheads')

        # number of reachable 9-height positions per trailhead
        trailhead_scores = []
        for trailhead in trailheads:

            print(f'exploring trailhead start {trailhead}')
            ans = bfs([trailhead])
            print(f'found trailhead start {trailhead} score of {ans}')

            trailhead_scores.append(ans)
        print(trailhead_scores)

        total_scores = sum(trailhead_scores)

        print(f'total trailhead scores {total_scores}')
        return total_scores

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

    assert 36 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 682 == answer
