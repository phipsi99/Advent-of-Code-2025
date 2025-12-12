from collections import defaultdict
from itertools import combinations
import numpy as np
from tqdm import tqdm
from helpers.get_input import get_lines

def print_coords(coordinates):
    max_x = max(x for x, y in coordinates)
    max_y = max(y for x, y in coordinates)
    grid = [["." for _ in range(max_x+1)] for _ in range(max_y+1)]

    for x, y in coordinates:
        grid[y][x] = "X"

    for row in grid:
        print(" ".join(row))

def rect_overlaps_border(grid, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    xs = slice(min(x1, x2), max(x1, x2)+1)
    ys = slice(min(y1, y2), max(y1, y2)+1)
    if grid[y1, xs].any() or grid[y2, xs].any() or grid[ys, x1].any() or grid[ys, x2].any():
        return True
    return False

def do_main(debug_mode=False):
    lines = get_lines('09', debug_mode)

    point_sum = 0
    tiles = []

    for line_index, line in enumerate(lines):
        tiles.append(tuple(int(i) for i in line.split(",")))

    rects = []
    pairs = combinations(tiles, 2)
    for pair1, pair2 in tqdm(pairs):
        dx = abs(pair1[0] - pair2[0]) + 1
        dy = abs(pair1[1] - pair2[1]) + 1
        rects.append(dx*dy)
    print(max(rects))

    # Build border
    border = defaultdict(list)
    for i in tqdm(range(len(tiles))):
        fresh_border = []
        dir = ''
        p1 = tiles[i]
        p2 = tiles[i+1] if i < len(tiles)-1 else tiles[0]
        if p1[0] == p2[0]:
            step = 1 if p1[1] < p2[1] else -1
            dir = 'right' if step == 1 else 'left'
            fresh_border = [(p1[0] , y) for y in range(p1[1], p2[1]+step, step)]
        else:
            step = 1 if p1[0] < p2[0] else -1
            dir = 'up' if step == 1 else 'down'
            fresh_border = [(x , p2[1]) for x in range(p1[0], p2[0]+step, step)]
        [border[b].append(dir) for b in fresh_border]

    # Explode border by 1 while excluding concave corners
    border[tiles[0]] = list(reversed(border[tiles[0]]))
    allowed_dirs = [['up', 'right'], ['right', 'down'], ['down', 'left'], ['left', 'up']]
    directions = {'up': (0, -1),'down': (0, 1),'left': (-1, 0),'right': (1, 0)}

    exploded_border = set()
    for coord in tqdm(border):
        dirs = border[coord]
        if len(dirs) == 1:
            exploded_border.add((coord[0]+directions[dirs[0]][0], coord[1]+directions[dirs[0]][1]))
        elif dirs in allowed_dirs:
                for dir in dirs:
                    exploded_border.add((coord[0]+directions[dir][0], coord[1]+directions[dir][1]))

    # Build a boolean grid containing the border
    max_x = max(x for x, y in exploded_border)
    max_y = max(y for x, y in exploded_border)
    grid = np.zeros((max_y+1, max_x+1), dtype=bool)
    for x, y in exploded_border:
        grid[y, x] = True

    rect_max = 0
    pairs = list(combinations(tiles, 2))
    for tile1, tile2 in tqdm(pairs):
        dx = abs(tile1[0] - tile2[0]) + 1
        dy = abs(tile1[1] - tile2[1]) + 1
        rect = dx*dy
        if rect <= rect_max:
            continue
        if rect_overlaps_border(grid, tile1, tile2):
            continue
        rect_max = rect
    print(rect_max)

if __name__ == '__main__':
    do_main(False)