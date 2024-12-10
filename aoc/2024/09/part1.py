from aoc.puzzle import Part1
from copy import copy

def unmap_disk(input_str):
    block_id = 0
    blocks = []
    for i in range(len(input_str)):
        print(f'i {i}')
        if i % 2 == 1:
            # even
            print(f'{i} is odd . append N times')
            for ii in range(int(input_str[i])):
                blocks.append('.')
        else:
            # odd
            print(f'{i} is even . append id={block_id} {input_str[i]} times')
            for ii in range(int(input_str[i])):
                blocks.append(str(block_id))
            block_id += 1
    # print(str(''.join(blocks)))
    return blocks

def defrag(blocks):
    defragged_blocks = copy(blocks)
    head, tail = 0, len(defragged_blocks)-1

    while head < tail:
        if defragged_blocks[head] == '.' and defragged_blocks[tail] != '.':
            # swap free space with block
            defragged_blocks[head], defragged_blocks[tail] = defragged_blocks[tail], defragged_blocks[head]
            head += 1
            tail -= 1
        elif defragged_blocks[head] == '.':
            tail -= 1
        else:
            head += 1
    # print(defragged_blocks)
    return defragged_blocks

class PuzzlePart1(Part1):
    def solve(self, input_str: str):
        blocks = unmap_disk(input_str.strip())
        defragged_blocks = defrag(blocks)

        # checksum
        return sum(i*int(val) for i, val in enumerate(defragged_blocks) if val != '.')

if __name__ == '__main__':
    puzzle = PuzzlePart1(2024, 9)

    assert '0..111....22222' == ''.join(unmap_disk('12345'))
    assert '00...111...2...333.44.5555.6666.777.888899' == ''.join(unmap_disk('2333133121414131402'))
    assert '0099811188827773336446555566..............' == ''.join(defrag(unmap_disk('2333133121414131402')))

    # puzzle.solve('12345')
    assert 1928 == puzzle.solve('2333133121414131402')

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 6446899523367 == answer
