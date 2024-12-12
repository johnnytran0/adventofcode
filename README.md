# adventofcode
https://adventofcode.com/

# Introduction

Welcome to my personal solutions for Advent of Code! My goal for 2024 is to participate in all the daily challenges to brush up my Python and problem-solving skills.

These solutions are cleaned-up first attempts and are unoptimized beyond what I needed to get my two daily stars.

## Progress

| Year                                                                        | Stars                                                                      |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| ![https://adventofcode.com/2024](https://img.shields.io/badge/🎄-2024-blue) | ![](https://img.shields.io/badge/%20%E2%AD%90-Work%20In%20Progress-yellow) |

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

class AoC(Puzzle):
    def solve(self, input: str):
        # logic
        pass

if __name__ == '__main__':
    puzzle = AoC(2024, 1, 1)
    answer = puzzle.solve(puzzle.input())
```
