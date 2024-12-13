from aoc.puzzle import Part1
import re

class AocPuzzle(Part1):
    def solve(self, input_str: str):

        def claw(machine):
            match_a = re.search(r'Button A: X\+(\d+), Y\+(\d+)', machine[0])
            match_b = re.search(r'Button B: X\+(\d+), Y\+(\d+)', machine[1])
            match_prize = re.search(r'Prize: X=(\d+), Y=(\d+)', machine[2])
            a_dx, a_dy = int(match_a.group(1)), int(match_a.group(2))
            b_dx, b_dy = int(match_b.group(1)), int(match_b.group(2))
            prize_x, prize_y = int(match_prize.group(1)), int(match_prize.group(2))

            # TODO
            det = a_dx*b_dy - a_dy*b_dx
            press_a = (prize_x*b_dy - prize_y*b_dx)/det
            press_b = (prize_y*a_dx - prize_x*a_dy)/det

            if press_a.is_integer() and press_b.is_integer() and (a_dx*press_a + b_dx*press_b, a_dy*press_a + b_dy*press_b) == (prize_x, prize_y):
                return 3*press_a + press_b
            else:
                return 0

        machines = [claw(machine.strip().splitlines()) for machine in input_str.strip().split('\n\n')]

        return int(sum(machines))

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 13)

    example_input = '''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
    '''

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 32026 == answer