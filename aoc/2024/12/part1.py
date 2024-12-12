from aoc.puzzle import Part1

class AocPuzzle(Part1):
    def solve(self, input_str: str):
        garden = [[col for col in row.strip()] for row in input_str.strip().splitlines()]
        rows, cols = len(garden), len(garden[0])

        visited = []
        regions = []

        def search(x,y, plant, region):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<rows and 0<=new_y<cols and (new_x, new_y) not in region and plant == garden[new_x][new_y]:
                    region.append((new_x,new_y))
                    search(new_x, new_y, plant, region)

        for x in range(rows):
            for y in range(cols):
                plot = (x, y)
                if plot not in visited:
                    plant = garden[x][y]
                    print(f'plot {plot} has plant {plant}')
                    curr_region = [plot]
                    search(x, y, plant, curr_region)
                    visited += curr_region

                    print(curr_region)
                    regions.append(curr_region)

        area = [sum(1 for _ in region) for region in regions]

        def perimeter(region):
            perim = 0
            for x,y in region:
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x+dx, y+dy
                    if (new_x, new_y) not in region:
                        perim += 1
            return perim

        perim = [perimeter(region) for region in regions]

        return sum(a*p for a,p in zip(area, perim))

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 12)

    example_input0 = '''
        AAAA
        BBCD
        BBCC
        EEEC
        '''

    example_input1 = '''
        RRRRIICCFF
        RRRRIICCCF
        VVRRRCCFFF
        VVRCCCJFFF
        VVVVCJJCFE
        VVIVCCJJEE
        VVIIICJJEE
        MIIIIIJJEE
        MIIISIJEEE
        MMMISSJEEE
        '''
    puzzle.solve(example_input0)
    assert 1930 == puzzle.solve(example_input1)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 1486324 == answer
