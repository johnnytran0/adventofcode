from aoc.puzzle import Part2
from statistics import variance
import re

# coprime
cols = 101
rows = 103

seconds = 100

class AocPuzzle(Part2):
    def solve(self, input_str: str):
        """
        uses https://en.wikipedia.org/wiki/Chinese_remainder_theorem
        :param input_str: initial position and velocity of each robot
        :return: num of seconds when Easter egg appears
        """
        def parse(robot):
            match = re.fullmatch(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', robot)
            p_x, p_y = int(match.group(2)), int(match.group(1))
            v_x, v_y = int(match.group(4)), int(match.group(3))
            return ((p_x, p_y), (v_x, v_y))

        robots = [parse(robot.strip()) for robot in input_str.strip().splitlines()]

        min_var_x = min(range(rows), key=lambda second: variance((p_x + v_x * second) % rows for (p_x, _), (v_x, _) in robots))
        min_var_y = min(range(cols), key=lambda second: variance((p_y + v_y * second) % cols for (_, p_y), (_, v_y) in robots))

        return min_var_x + ((pow(rows, -1, cols) * (min_var_y - min_var_x)) % cols) * rows

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 14)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 7371 == answer
