from aoc.puzzle import Puzzle
import bisect

class Part1(Puzzle):
    def solve(self, input: str):
        '''
        pair up the numbers and measure how far apart they are
        add up all those distances to find the total distance between the left and right list
        '''

        # parse input to left and right list
        left, right = [], []
        lines = input.strip().split('\n')
        for line in lines:
            if line:
                line_split = line.strip().split(' ')
                bisect.insort(left, int(line_split[0]))
                bisect.insort(right, int(line_split[-1]))

        return sum([abs(x-y) for x, y in zip(left, right)])

if __name__ == '__main__':
    puzzle1 = Part1(2024, 1, 1)

    example_input = '''
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    '''
    assert 11 == puzzle1.solve(example_input)

    answer = puzzle1.solve(puzzle1.input())
    print(f'answer: {answer}')
    assert 1590491 == answer
