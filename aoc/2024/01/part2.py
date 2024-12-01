from aoc.puzzle import Puzzle
import bisect

class Part2(Puzzle):
    def solve(self, input: str):
        '''
        Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
        '''

        # parse input to left and right list
        left, right = [], []
        lines = input.strip().split('\n')
        for line in lines:
            if line:
                line_split = line.strip().split(' ')
                bisect.insort(left, int(line_split[0]))
                bisect.insort(right, int(line_split[-1]))

        # calculate total similarity
        return sum([left_num*right.count(left_num) for left_num in left])

if __name__ == '__main__':
    puzzle = Part2(2024, 1, 2)

    example_input = '''
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    '''
    assert 31 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 22588371 == answer
