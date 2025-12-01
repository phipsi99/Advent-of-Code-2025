from pathlib import Path


def do_main(debug_mode=False):
    with open(Path("01/input.txt")) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path("01/test.txt")) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    point_sum2 = 0

    pointer = 50

    for line_index, line in enumerate(lines):
        num = int(line[1:])
        if line.startswith("L"):
            if pointer - num <= 0:
                if pointer != 0:
                    point_sum2 += 1
                point_sum2 += (abs(pointer - num)) // 100
            pointer = (pointer - num) % 100
        else:
            if pointer + num > 99:
                point_sum2 += (pointer + num) // 100
            pointer = (pointer + num) % 100

        if pointer == 0:
            point_sum += 1

    print(point_sum)
    print(point_sum2)


if __name__ == "__main__":
    do_main(False)
