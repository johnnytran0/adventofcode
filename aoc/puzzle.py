import os
from abc import ABC, abstractmethod

from aoc.helpers import read_input_file, request_input_file

class Puzzle(ABC):
    def __init__(self, year: int, day: int, part: int, input_file_path = None) -> None:
        self.year = year
        self.day = day
        self.part = part
        self.year = year
        self.input_file_path = input_file_path
        super().__init__()

    @abstractmethod
    def solve(self, input: str):
        pass

    def input(self) -> str:
        '''
        retrieves input from web or local file
        :return: contents of input
        '''
        if 'AOC_SESSION' in os.environ:
            return request_input_file(self.year, self.day)

        if self.input_file_path:
            return read_input_file(self.input_file_path)
        else:
            raise Exception('input_file_path is not specified')
