from itertools import combinations
import math
from helpers.get_input import get_lines
import networkx as nx


def do_main(debug_mode=False):
    lines = get_lines('08', debug_mode)

    point_sum = 0
    range_pairs = 10 if debug_mode else 1000
    boxes = []

    for line_index, line in enumerate(lines):
        boxes.append([int(i) for i in line.split(",")])

    pairs = combinations(boxes, 2)
    distances = {}

    for box1, box2 in pairs:
        dist = math.dist(box1, box2)
        distances[dist] = (box1, box2)
    sorted_distances = sorted(distances.items())

    graph = nx.Graph()
    for i in range(len(sorted_distances)):
        box1, box2 = (tuple(x) for x in sorted_distances[i][1])
        if i == range_pairs:
            components = list(nx.connected_components(graph))
            lens = sorted([len(c) for c in components])
            print(math.prod(lens[-3:]))
        if graph.has_node(box1) and graph.has_node(box2) and nx.has_path(graph, box1, box2):
            continue
        graph.add_edge(box1, box2)
        if len(list(nx.connected_components(graph))[0]) == len(boxes):
                print(box1[0] * box2[0])
                break

if __name__ == '__main__':
    do_main(False)