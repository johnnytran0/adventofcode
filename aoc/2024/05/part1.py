from aoc.puzzle import Part1
from collections import defaultdict

def is_correct(update: list[int], rules: dict[int, set[int]]) -> bool:
    """
    for every page number in update, ensure subsequent page number does not break rule.
    :param update: list of page numbers to update
    :param rules: dict of page number to set of numbers that must occur before
    :return: True if all page numbers are ruled correct
    """
    for i in range(len(update)-1):
        current_page = update[i]
        current_rule = rules[current_page]
        if any(set(update[i+1:]).intersection(current_rule)):
            return False
    return True

class PuzzlePart1(Part1):
    def solve(self, input_str: str):
        """
        notation X|Y means that if both page number X and page number Y are to be produced as part of an update,
        page number X must be printed at some point before page number Y.
        :param input_str: page ordering rules and the pages to produce in each update
        :return: sum of middle page numbers for all correct updates
        """
        sections = input_str.split('\n\n')

        # parse rules
        page_ordering_rules = [tuple(map(int, l.strip().split('|'))) for l in sections[0].splitlines() if l.strip()]

        rules_dict = defaultdict(set)
        # keys must not occur before elements in value
        for x, y in page_ordering_rules:
            rules_dict[y].add(x)

        pages_to_produce = [[int(l2) for l2 in l.strip().split(',')] for l in sections[1].splitlines() if l.strip()]
        correctly_ordered_updates = [p for p in pages_to_produce if is_correct(p, rules_dict)]
        return sum(update[len(update)//2] for update in correctly_ordered_updates)

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

    example_answer = puzzle.solve(puzzle.input())
    print(f'answer: {example_answer}')
    assert 4774 == example_answer
