from aoc.puzzle import Part2

def unmap_disk(input_str):
    block_id = 0
    blocks = []
    for i in range(len(input_str)):
        if i % 2 == 1:
            for ii in range(int(input_str[i])):
                blocks.append('.')
        else:
            for ii in range(int(input_str[i])):
                blocks.append(str(block_id))
            block_id += 1
    return blocks

def defrag(blocks):

    def get_last_target_block(block3, target: int):
        i, j = 0, len(block3) - 1
        while i < j:
            if block3[j] == '.' or block3[j] != str(target):
                j -=1
            else:
                block_id2 = block3[j]
                block_start2 = block_end2 = j
                while 0 < block_start2-1 and block3[block_start2 - 1] == block_id2:
                    block_start2 -=1
                print(f'found block_id={block_id2} from index {block_start2}-{block_end2} of len {block_end2-block_start2+1}')
                return block_start2, block_end2

    def alloc(block2, free_space):
        space_start2 = 0
        while space_start2 < len(block2) - 1:
            if block2[space_start2] == '.':
                space_end2 = space_start2 + free_space
                if space_end2 < len(block2) and all(block2[ii] == '.' for ii in range(space_start2, space_end2)):
                    return space_start2, space_end2
                else:
                    space_start2 += 1
            else:
                space_start2 += 1
        return None, None

    def get_last_block_id(block1):
        i, j = 0, len(block1) - 1
        while i < j:
            if block1[j] == '.':
                j -=1
            else:
                block_id2 = block1[j]
                return block_id2
        return 0

    max_block_id = get_last_block_id(blocks)
    for block_id in range(1, int(max_block_id)+1)[::-1]:
        b_start, b_end = get_last_target_block(blocks, block_id)
        s_start, s_end = alloc(blocks, b_end-b_start+1)
        if s_start is not None and s_end is not None and s_start < b_start:
            blocks[s_start:s_end], blocks[b_start:b_end+1] = blocks[b_start:b_end+1], blocks[s_start:s_end]

    return blocks

class PuzzlePart2(Part2):
    def solve(self, input_str: str):
        return sum(i*int(val) for i, val in enumerate(defrag(unmap_disk(input_str.strip()))) if val != '.')

if __name__ == '__main__':
    puzzle = PuzzlePart2(2024, 9)

    assert 2858 == puzzle.solve('2333133121414131402')

    answer = puzzle.solve(puzzle.input())
    print(f'answer: {answer}')
    assert 6446899523367 == answer
