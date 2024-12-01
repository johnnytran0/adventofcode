import os
import requests
import requests_cache
import sys

requests_cache.install_cache('aoc_cache', expire_after=3600 )

def request_input_file(year:int, day: int):
    '''
     Request puzzle input file for specified year & day from adventofcode.com.
     Requires AOC_SESSION env var is set and valid.
    :param year: puzzle year
    :param day: puzzle day
    :return: input file contents
    '''
    assert 'AOC_SESSION' in os.environ, 'AOC_SESSION must be set with valid session cookie'

    session = os.getenv('AOC_SESSION')
    headers = {'Cookie': f'session={session}'}

    url = f'https://adventofcode.com/{year}/day/{day}/input'

    print(f'making request to {url}')
    r = requests.get(url, headers=headers)

    if r.ok:
        return r.text
    else:
        raise Exception(f'API error with status code={r.status_code}: {r.reason}\n{r.content}')

def read_input_file(file_path) -> str:
    '''
     Reads puzzle input file from given file path.
    :param file_path: path to input
    :return: file contents
    '''
    with open(file_path) as file:
        print(f'reading input file at {file_path}')
        return file.read()
