from pathlib import Path
import re
from tqdm import tqdm
from helpers.get_input import get_lines


def do_main(debug_mode=False):
    lines = get_lines('02')

    point_sum = 0
    point_sum2 = 0

    ranges = [(int(l.split("-")[0]), int(l.split("-")[1])) for l in lines[0].split(",")]

    for r_min, r_max in tqdm(ranges):
        for x in tqdm(range(r_min, r_max+1)):
            if re.fullmatch(r"(\d+)\1", str(x)):
                point_sum += x
            if re.fullmatch(r"(\d+)\1+", str(x)):
                point_sum2 += x

    print(point_sum)
    print(point_sum2)

if __name__ == '__main__':
    do_main(False)