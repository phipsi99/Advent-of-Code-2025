from matplotlib import pyplot as plt
import numpy as np
from helpers.get_input import get_lines

directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

def do_main(debug_mode=False):
    lines = get_lines('04', debug_mode)

    point_sum = 0

    paper_rolls = np.array([list(line) for line in lines])

    for y in range(paper_rolls.shape[0]):
        for x in range(paper_rolls.shape[1]):
            if paper_rolls[y,x] != '@':
                continue
            adjectent_count = 0
            for dx, dy in directions:
                if not (0 <= y+dy < paper_rolls.shape[0] and 0 <= x+dx < paper_rolls.shape[1]):
                    continue
                if paper_rolls[y+dy,x+dx] == '@':
                    adjectent_count += 1
            if adjectent_count < 4:
                point_sum += 1
    print(point_sum)


    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow((paper_rolls == '@').astype(int), cmap='Greens')

    removal_count_old = -1
    removal_count_new = 0

    while removal_count_new != removal_count_old:
        removal_count_old = removal_count_new
        rolls_to_remove = []
        for y in range(paper_rolls.shape[0]):
            for x in range(paper_rolls.shape[1]):
                if paper_rolls[y,x] != '@':
                    continue
                adjectent_count = 0
                for dx, dy in directions:
                    if not (0 <= y+dy < paper_rolls.shape[0] and 0 <= x+dx < paper_rolls.shape[1]):
                        continue
                    if paper_rolls[y+dy,x+dx] == '@':
                        adjectent_count += 1
                if adjectent_count < 4:
                    rolls_to_remove.append((y,x))
        for remy, remx in rolls_to_remove:
            paper_rolls[remy, remx] = '.'
        removal_count_new += len(rolls_to_remove)
        im.set_data((paper_rolls == '@').astype(int))
        plt.draw()
        plt.pause(0.3)

    plt.ioff()
    plt.show()
    print(removal_count_new)

if __name__ == '__main__':
    do_main(False)