from aoc.puzzle import Puzzle

class Part1(Puzzle):
    def is_safe(self, level_diffs: list) -> bool:
        '''
        any two adjacent numbers differ by at least one and at most 3
        :param diffs: list of integer difference between sequential levels
        :return: if the record is safe
        '''
        if all(0 < diff for diff in level_diffs):
            return all(1 <= diff <= 3 for diff in level_diffs)
        elif all(diff < 0 for diff in level_diffs):
            return all(1 <= abs(diff) <= 3 for diff in level_diffs)
        else:
        # 0 in record
            return False

    def solve(self, input_str: str):
        '''
        one report per line, consisting of a list of numbers called levels that are space separated.
        a report only counts as safe if both of the following are true:
        * levels are either all increasing or all decreasing
        * any two adjacent levels differ by at least one and at most 3
        how many reports are safe?
        '''
        reports = [[int(num) for num in report.strip().split()] for report in input_str.strip().splitlines()]
        print(reports)

        safe_reports = [self.is_safe([y-x for x,y in zip(report, report[1:])]) for report in reports]
        print(safe_reports)

        return sum(safe_reports)

if __name__ == '__main__':
    puzzle = Part1(2024, 2, 1)

    example_input = '''
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    '''
    assert 2 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 598 == answer
