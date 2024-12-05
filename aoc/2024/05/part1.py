from aoc.puzzle import Part1

class PuzzlePart1(Part1):
    def solve(self, input_str: str):
        pass

if __name__ == '__main__':
    puzzle = PuzzlePart1(2024, 5)

    example_input = '''
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13

        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        75,97,47,61,53
        61,13,29
        97,13,75,29,47
        '''

    assert 143 == puzzle.solve(example_input)

    # answer = puzzle.solve(puzzle.input())
    # print(f'answer: {answer}')
