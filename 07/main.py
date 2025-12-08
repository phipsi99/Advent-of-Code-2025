from copy import deepcopy
from functools import cache
from tqdm import tqdm
from helpers.get_input import get_lines
import networkx as nx
import matplotlib.pyplot as plt

def count_paths_dfs(graph: nx.DiGraph, start, end):
    @cache
    def dfs(start, end):
        if start == end:
            return 1
        count = 0
        for neighbor in graph.successors(start):
            count += dfs(neighbor, end)
        return count
    return(dfs(start, end))

def do_main(debug_mode=False):
    lines = get_lines('07', debug_mode)

    point_sum = 0
    grid = ["" for _ in range(len(lines))]

    for line_index, line in enumerate(lines):
        grid[line_index] = list(line)

    graph = nx.DiGraph()
    start = ()

    new_grid = deepcopy(grid)
    for row_index, row in enumerate(grid[1:]):
        for col_index, val in enumerate(row):
            above = new_grid[row_index][col_index]
            if above == '|' or above == 'S':
                if above == 'S':
                    start = (row_index, col_index)
                if val == '.':
                    new_grid[row_index+1][col_index] = '|'
                    graph.add_edge((row_index, col_index), (row_index+1, col_index))
                elif val == '^':
                    new_grid[row_index+1][col_index-1] = '|'
                    new_grid[row_index+1][col_index+1] = '|'
                    graph.add_edge((row_index, col_index), (row_index+1, col_index-1))
                    graph.add_edge((row_index, col_index), (row_index+1, col_index+1))
                    point_sum += 1
    print(point_sum)
    path_num = 0
    sinks = [n for n in graph if graph.out_degree(n) == 0]
    for s in tqdm(sinks):
        path_num += count_paths_dfs(graph, start, s)
    print(path_num)

if __name__ == '__main__':
    do_main(False)