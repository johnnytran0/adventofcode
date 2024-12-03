from aoc.puzzle import Part2
import re

class PuzzlePart2(Part2):
    def eval_mul(self, mul: str) -> int:
        """
        the goal of the program is just to multiply some numbers.
        mul instructions look like mul(X,Y), where X and Y are each 1-3 digit numbers.

        examples:
            mul(1,2)
            mul(123,456)
        :param mul: valid mul instruction string
        :return: int value of evaluating the instruction
        """
        # parse
        args = mul[4:-1].split(',')
        a, b = int(args[0]), int(args[1])

        return a * b

    def solve(self, input_str: str):
        """
        The do() instruction enables future mul instructions.
        The don't() instruction disables future mul instructions.
        At the beginning of the program, mul instructions are enabled.
        :param input_str: corrupted memory string
        :return: sum of all valid enabled mul instructions
        """
        # parse input_str for valid instructions
        instruction_regex = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)')
        valid_instructions = re.findall(instruction_regex, input_str)

        enabled, enabled_muls = True, []

        for instr in valid_instructions:
            if enabled:
                if instr == "don't()":
                    enabled = False
                elif instr.startswith("mul("):
                    enabled_muls.append(instr)
            else:
                if instr == "do()":
                    enabled = True

        return sum(self.eval_mul(mul) for mul in enabled_muls)

if __name__ == '__main__':
    puzzle = PuzzlePart2(2024, 3)

    example_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert 48 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 79845780 == answer
