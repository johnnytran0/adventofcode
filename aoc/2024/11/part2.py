from aoc.puzzle import Part2
from collections import defaultdict

blinks = 75

class AocPuzzle(Part2):
    def solve(self, input_str: str):
        stones = defaultdict(int)
        for stone in input_str.strip().split():
            stones[stone] = 1

        def change_stone(stone):
                if stone == '0':
                    new_stones['1'] += stones['0']
                elif len(stone) % 2 == 0:
                    middle = len(stone) // 2
                    new_stones[str(int(stone[:middle]))] += stones[stone]
                    new_stones[str(int(stone[middle:]))] += stones[stone]
                else:
                    new_stones[str(int(stone) * 2024)] += stones[stone]

        for blink in range(blinks):
            new_stones = defaultdict(int)
            for stone in stones.keys():
                change_stone(stone)
            stones = new_stones

        return sum(count for count in stones.values())

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 11)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 277444936413293 == answer
