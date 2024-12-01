# adventofcode
https://adventofcode.com/

# Setup
1. Login in to [AoC](https://adventofcode.com/)
1. Open Developer Tools and view Cookies
1. Copy the `session` token value to the `AOC_SESSION` env var on your local.

# Getting Started
```bash
pip install -r requirements.txt
```

## Template
```python
from aoc.puzzle import Puzzle

class Part1(Puzzle):
    def solve(self, input: str):
        # logic
        pass

if __name__ == '__main__':
    puzzle = Part1(2024, 1, 1)
    answer = puzzle.solve(puzzle.input())
```
