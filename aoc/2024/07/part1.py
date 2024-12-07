from aoc.puzzle import Part1
import re

operators = ('+', '*')

def valid(test_val: int, vals: list[int]) -> bool:
    print(f'{test_val}: {vals}')

    def eval(nums, ops):
        total = nums.pop(0)

        while nums and ops:
            val = nums.pop(0)
            op = ops.pop(0)

            total = math(total, op, val)
        return total

    def search(vals, num_stack, op_stack):
        if not vals:
            print(f'{vals} {num_stack} {op_stack}')
            res = eval(num_stack, op_stack)
            return test_val == res
        else:
            return any(search(vals[1:], num_stack + [vals[0]], op_stack + [new_op]) for new_op in operators)

    if not vals:
        return False
    elif len(vals) == 1:
        return test_val == vals[0]
    else:
        assert len(vals) >= 2
        return search(vals[1:], [vals[0]], [])

def math(a: int, op: str, b: int) -> int:
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    return -1

class PuzzlePart1(Part1):
    def solve(self, input_str: str):
        """
        operators are always eval left to right, not according to precedence
        numbers in eq can't be rearranged
        :param input_str: calibration equations
        :return: total calibration result, sum of test values in all equations that are valid
        """
        eqs_raw = [re.split(r':\s+', eq.strip()) for eq in input_str.strip().splitlines()]
        eqs_dict = {eq2[0]: eq2[1].split() for eq2 in eqs_raw}
        valid_eqs = [int(eq[0]) for eq in eqs_dict.items() if valid(int(eq[0]), [int(i) for i in eq[1]])]
        return sum(valid_eqs)

if __name__ == '__main__':
    puzzle = PuzzlePart1(2024, 7)

    example_input = '''
        190: 10 19
        3267: 81 40 27
        83: 17 5
        156: 15 6
        7290: 6 8 6 15
        161011: 16 10 13
        192: 17 8 14
        21037: 9 7 18 13
        292: 11 6 16 20
        '''

    assert 3749 == puzzle.solve(example_input)

    example_answer = puzzle.solve(puzzle.input())
    print(f'answer: {example_answer}')
    assert 12940396350192 == example_answer
