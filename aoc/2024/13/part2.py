from aoc.puzzle import Part2
import re

class AocPuzzle(Part2):
    def solve(self, input_str: str):

        def claw(machine, offset):
            """
            uses Cramer's Rule
            :param machine: claw machine input
            :return: minimum tokens to win prize
            """
            match_a = re.search(r'Button A: X\+(\d+), Y\+(\d+)', machine[0])
            match_b = re.search(r'Button B: X\+(\d+), Y\+(\d+)', machine[1])
            match_prize = re.search(r'Prize: X=(\d+), Y=(\d+)', machine[2])
            a_dx, a_dy = int(match_a.group(1)), int(match_a.group(2))
            b_dx, b_dy = int(match_b.group(1)), int(match_b.group(2))
            prize_x, prize_y = int(match_prize.group(1)) + offset, int(match_prize.group(2)) + offset

            determinant = a_dx*b_dy - a_dy*b_dx
            press_a = (prize_x*b_dy - prize_y*b_dx)/determinant
            press_b = (prize_y*a_dx - prize_x*a_dy)/determinant

            if press_a.is_integer() and press_b.is_integer() and (a_dx*press_a + b_dx*press_b, a_dy*press_a + b_dy*press_b) == (prize_x, prize_y):
                return 3*press_a + press_b
            else:
                return 0

        machines = [claw(machine.strip().splitlines(), 10000000000000) for machine in input_str.strip().split('\n\n')]

        return int(sum(machines))

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 13)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 89013607072065 == answer
