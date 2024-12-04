from aoc.puzzle import Part2

def eq_mas(char_list: list[str]) -> bool:
    test_str = ''.join(char_list)
    return test_str == 'MAS' or test_str[::-1] == 'MAS'

class PuzzlePart2(Part2):
    def solve(self, input_str: str):
        """
        find two MAS in the shape of an X, each MAS can be written forwards or backwards
        :param input_str: word search input will be full of letters
        :return: count of valid occurrences of X-MAS pattern in the input string
        """
        matrix = [[letter for letter in line.strip()] for line in input_str.strip().splitlines()]
        num_rows, num_cols = len(matrix), len(matrix[0])

        xmas = 0

        for r in range(1, num_rows-1):
            for c in range(1, num_cols-1):
                letter = matrix[r][c]
                if letter == 'A':
                    print(f'({r},{c}): {matrix[r][c]}')

                    back_slash = [matrix[r-1][c-1], matrix[r][c], matrix[r+1][c+1]]
                    forward_slash = [matrix[r-1][c+1], matrix[r][c], matrix[r+1][c-1]]

                    if eq_mas(back_slash) and eq_mas(forward_slash):
                        xmas += 1

        return xmas

if __name__ == '__main__':
    puzzle = PuzzlePart2(2024, 4)

    example_input = '''
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    '''

    assert 9 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 1880 == answer
