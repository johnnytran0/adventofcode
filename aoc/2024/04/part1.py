from aoc.puzzle import Part1

def eq_xmas(char_list: list[str]) -> bool:
    return ''.join(char_list) == 'XMAS'

class PuzzlePart1(Part1):
    def solve(self, input_str: str):
        """
        This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
        Find all instances of the word XMAS
        :param input_str: word search input will be full of letters
        :return: count of valid occurrences of the word XMAS in the input string
        """
        matrix = [[letter for letter in line.strip()] for line in input_str.strip().splitlines()]

        num_rows, num_cols = len(matrix), len(matrix[0])
        first_row, last_row = 0, num_rows - 1
        first_col, last_col = 0, num_cols - 1

        xmas = 0

        for r in range(num_rows):
            for c in range(num_cols):
                letter = matrix[r][c]
                if letter == 'X':
                    print(f'({r},{c}): {matrix[r][c]}')

                    # horizontal
                    # forward
                    if c+3 <= last_col and eq_xmas([matrix[r][c], matrix[r][c+1], matrix[r][c+2], matrix[r][c+3]]):
                        xmas += 1

                    # backwards
                    if first_col <= c-3 and eq_xmas([matrix[r][c], matrix[r][c-1], matrix[r][c-2], matrix[r][c-3]]):
                        xmas += 1

                    # vertical
                    # up
                    if first_row <= r-3 and eq_xmas([matrix[r][c], matrix[r-1][c], matrix[r-2][c], matrix[r-3][c]]):
                        xmas += 1
                    # down
                    if r+3 <= last_row and eq_xmas([matrix[r][c], matrix[r+1][c], matrix[r+2][c], matrix[r+3][c]]):
                        xmas += 1

                    # diagonal
                    # 45 deg
                    if first_row <= r-3 and c+3 <= last_col and eq_xmas([matrix[r][c], matrix[r-1][c+1], matrix[r-2][c+2], matrix[r-3][c+3]]):
                        xmas += 1
                    # 135 deg
                    if first_row <= r-3 and first_col <= c-3 and eq_xmas([matrix[r][c], matrix[r-1][c-1], matrix[r-2][c-2], matrix[r-3][c-3]]):
                        xmas += 1
                    # 225 deg
                    if r + 3 <= last_row and first_col <= c - 3 and eq_xmas([matrix[r][c], matrix[r + 1][c - 1], matrix[r + 2][c - 2], matrix[r + 3][c - 3]]):
                        xmas += 1
                    ## 315 deg
                    if r+3 <= last_row and c+3 <= last_col and eq_xmas([matrix[r][c], matrix[r+1][c+1], matrix[r+2][c+2], matrix[r+3][c+3]]):
                        xmas += 1

        return xmas

if __name__ == '__main__':
    puzzle = PuzzlePart1(2024, 4)

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

    assert 18 == puzzle.solve(example_input)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 2591 == answer
