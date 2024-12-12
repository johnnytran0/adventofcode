from aoc.puzzle import Part2

# coordinate offsets to check corner pairs for (x,y): top-left, top-right, bottom-right, bottom-left
CORNER_PAIRS = [((-1, 0), (0, -1)), ((0, -1), (1, 0)), ((1, 0), (0, 1)), ((0, 1), (-1, 0))]

class AocPuzzle(Part2):
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

        def sides(region):
            """
            for 2D closed polygons, sides == corners
            :param region: list of coordinates in region
            :return: number of sides in region
            """
            corners = 0

            for x,y in region:
                for (dx1, dy1), (dx2, dy2) in CORNER_PAIRS:
                    adj_plot_a = (x+dx1, y+dy1)
                    adj_plot_b = (x+dx2, y+dy2)
                    if adj_plot_a not in region and adj_plot_b not in region:
                        print(f'found outside corner for {garden[x][y]} at {x,y}')
                        corners += 1
                    diagonal_plot = (x + dx1 + dx2, y + dy1 + dy2)
                    if adj_plot_a in region and adj_plot_b in region and diagonal_plot not in region:
                        print(f'found inside corner for {garden[x][y]} at {x,y}')
                        corners += 1

            return corners

        sides = [sides(region) for region in regions]

        return sum(a*p for a,p in zip(area, sides))

if __name__ == '__main__':
    puzzle = AocPuzzle(2024, 12)

    example_input0 = '''
        AAAA
        BBCD
        BBCC
        EEEC
        '''
    assert 80 == puzzle.solve(example_input0)

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
    assert 1206 == puzzle.solve(example_input1)

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 898684 == answer
