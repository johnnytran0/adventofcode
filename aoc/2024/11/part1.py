from aoc.puzzle import Part1

blinks = 25
def change_stone(stone):
    if int(stone) == 0:
        return [str(1)]
    elif len(stone) % 2 == 0:
        middle = len(stone) // 2
        return [str(int(stone[:middle])), str(int(stone[middle:]))]
    else:
        return [str(int(stone)*2024)]

class AocPuzzle(Part1):
    def solve(self, input_str: str):
        stones = input_str.split()

        for i in range(blinks):
            new_stones = []
            for stone in stones:
                new_stones.extend(change_stone(stone))
            stones = new_stones

        return len(stones)

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 11)

    assert 55312 == puzzle.solve('125 17')

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 233875 == answer
