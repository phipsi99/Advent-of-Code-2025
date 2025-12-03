from pathlib import Path
import requests
import os

def get_lines(day, debug_mode = False):
    with open(Path(f'{day}/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    if not lines:
        lines = [line.rstrip() for line in get_input(day).splitlines()]
        with open(Path(f'{day}/input.txt'), 'w') as file:
            file.writelines([line + '\n' for line in lines])
    if debug_mode:
        with open(Path(f'{day}/test.txt')) as file:
            lines = [line.rstrip() for line in file]
    return lines


def get_input(day):
    day = int(day)
    session_token = os.getenv('AOC_SESSION_TOKEN')
    url = f'https://adventofcode.com/2025/day/{day}/input'
    headers = {'Cookie': f'session={session_token}'}
    r = requests.get(url, headers=headers, verify=False)

    if r.status_code == 200:
        return r.text
    else:
        print(f"Error: {r.status_code}: {r.reason} \n{r.content}")


if __name__== "__main__":
    print(get_input(1))