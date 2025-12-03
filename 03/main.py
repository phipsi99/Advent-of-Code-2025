from helpers.get_input import get_lines


def get_max_joltage(bat, n):
    jol_str = ""
    new_bat = bat[:]
    for m in range(n, 0, -1):
        slice_end = -(m-1)
        if m == 1:
            slice_end = len(new_bat)
        next_max = max(new_bat[:slice_end])
        last_index = new_bat.index(next_max)
        new_bat = new_bat[last_index+1:]
        jol_str += str(next_max)
    print(jol_str)
    return int(jol_str)

def do_main(debug_mode=False):
    lines = get_lines('03', debug_mode)

    point_sum = 0
    point_sum2 = 0

    for line_index, line in enumerate(lines):
        r = [int(i) for i in line]
        jol = get_max_joltage(r, 2)
        jol2 = get_max_joltage(r, 12)
        point_sum+=jol
        point_sum2+=jol2

    print(point_sum)
    print(point_sum2)

if __name__ == '__main__':
    do_main(False)