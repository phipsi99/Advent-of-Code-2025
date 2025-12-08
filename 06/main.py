import numpy as np
from helpers.get_input import get_lines

def calc(nums, op):
    if op == "+":
        return np.sum(nums)
    else:
        return np.prod(nums)

def do_main(debug_mode=False):
    lines = get_lines('06', debug_mode)
    max_len = max(len(line) for line in lines)
    lines = [line.ljust(max_len) for line in lines]

    point_sum = 0

    point_sum = 0
    rows = [l.split() for l in lines]
    reversed = zip(*rows)

    for row in reversed:
        numbers = [int(x) for x in row[:-1]]
        point_sum += calc(numbers, row[-1])
    print(point_sum)

    point_sum = 0
    rows = [list(l) for l in lines]
    reversed = list(zip(*rows))
    i=0
    numbers = []
    operand = ''
    while i < len(reversed):
        if not ''.join(reversed[i]).strip():
            point_sum += calc(numbers, operand)
            numbers = []
            operand = ''
            i += 1
            continue
        if reversed[i][-1].strip():
            operand = reversed[i][-1]
        numbers.append(int(''.join(reversed[i][:-1])))
        i += 1
    point_sum += calc(numbers, operand)

    print(point_sum)

if __name__ == '__main__':
    do_main(False)