from pathlib import Path
import re
import numpy as np
import numpy as np

import numpy as np

def do_main(debug_mode=False):
    with open(Path(f'12/input.txt')) as file:
        text = file.read()
    if debug_mode:
        with open(Path(f'12/test.txt')) as file:
            text = file.read()

    blocks = text.strip().split("\n\n")
    presents = []
    regions = []

    for block in blocks:
        lines = block.splitlines()
        if 'x' in lines[0]:
            for line in lines:
                m = re.match(r"(\d+)x(\d+):\s*((?:\d+\s*)+)", line)
                dims = (int(m.group(2)), int(m.group(1)))
                values = list(map(int, m.group(3).split()))
                regions.append((dims, values))
            break
        arr = np.array([[1 if c == '#' else 0 for c in line] for line in lines[1:]])
        presents.append(arr)

    valid = 0
    counts = [np.count_nonzero(p) for p in presents]
    for dim, values in regions:
        maxp = dim[0]*dim[1]
        p = sum([v*counts[i] for i, v in enumerate(values)])
        if p > maxp:
            continue
        valid += 1
    print(valid)


if __name__ == '__main__':
    do_main(False)