from aoc.puzzle import Part1
import re

class PuzzlePart1(Part1):
    def eval_mul(self, mul: str) -> int:
        """
        mul(1,2)
        mul(123,456)
        :param mul:
        :return:
        """
        # parse
        args = mul[4:-1].split(',')
        a, b = int(args[0]), int(args[1])

        return a * b

    def solve(self, input_str: str):
        """
        the goal of the program is just to multiply some numbers.
        It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.
        there are also many invalid characters that should be ignored, even if they look like part of a mul instruction.
        Scan the corrupted memory for uncorrupted mul instructions.
        What do you get if you add up all the results of the multiplications?

        :param input_str: corrupted string to parse valid mul instructions
        :return: sum of the output of all valid mul instructions
        """
        # parse input_str for valid muls
        valid_mul_regex = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)')
        valid_muls = re.findall(valid_mul_regex, input_str)

        return sum(self.eval_mul(mul) for mul in valid_muls)

if __name__ == '__main__':
    puzzle = PuzzlePart1(2024, 3)

    assert 2 * 4 == puzzle.eval_mul('mul(2,4)')

    example_input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    print(puzzle.solve(example_input))
    assert 161 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 157621318 == answer
