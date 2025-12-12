from functools import cache
from pathlib import Path
import re
from tqdm import tqdm
from helpers.get_input import get_lines
import networkx as nx


def dfs_with_memo2(graph: nx.DiGraph):
    @cache
    def dfs(start, end, passed_dac, passed_fft):
        if start == end:
            return 1 if passed_dac and passed_fft else 0
        count = 0
        if start == 'dac':
            passed_dac = True
        if start == 'fft':
            passed_fft = True
        for n in graph.successors(start):
            count += dfs(n, end, passed_dac, passed_fft)
        return count

    return dfs('svr', 'out', False, False)

def dfs_with_memo1(graph: nx.DiGraph):
    @cache
    def dfs(start, end):
        if start == end:
            return 1
        count = 0
        for n in graph.successors(start):
            count += dfs(n, end)
        return count

    return dfs('you', 'out')

def do_main(debug_mode=False):
    lines = get_lines('11', debug_mode)

    graph = nx.DiGraph()

    for line_index, line in enumerate(lines):
        r = re.findall(r'[a-z]{3}', line)
        for rr in r[1:]:
            graph.add_edge(str(r[0]), str(rr))

    print(dfs_with_memo1(graph))
    print(dfs_with_memo2(graph))

if __name__ == '__main__':
    do_main(False)