from pathlib import Path
import re
from tqdm import tqdm
from helpers.get_input import get_lines


def do_main(debug_mode=False):
    lines = get_lines('08', debug_mode)

    point_sum = 0

    for line_index, line in enumerate(lines):
        r = [int(i) for i in line.split(" ")]

if __name__ == '__main__':
    do_main(False)