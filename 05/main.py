from tqdm import tqdm
from helpers.get_input import get_lines


def do_main(debug_mode=False):
    lines = get_lines('05', debug_mode)

    point_sum = 0
    fresh_ranges = []
    to_test = []

    for line_index, line in enumerate(lines):
        if "-" in line:
            fresh_ranges.append(tuple(int(r) for r in line.split("-")))
        elif line.rstrip():
            to_test.append(int(line))


    fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    cleaned_ranges = [fresh_ranges[0]]
    for rmin, rmax in fresh_ranges[1:]:
        lastmin, lastmax = cleaned_ranges[-1]
        if rmin <= lastmax:
            cleaned_ranges[-1] = lastmin, max(rmax, lastmax)
        else:
            cleaned_ranges.append((rmin, rmax))

    for i in tqdm(to_test):
        for rmin, rmax in cleaned_ranges:
            if rmin <= i <= rmax:
                point_sum += 1
                break
    print(point_sum)

    total_fresh = 0
    for rmin, rmax in cleaned_ranges:
        total_fresh += rmax-rmin+1

    print(total_fresh)

if __name__ == '__main__':
    do_main(False)