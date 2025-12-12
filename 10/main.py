from collections import deque
import re
import numpy as np
from tqdm import tqdm
from helpers.get_input import get_lines
import pulp


def do_main(debug_mode=False):
    lines = get_lines('10', debug_mode)

    point_sum = 0

    machines = []

    for line_index, line in enumerate(lines):
        pattern = re.search(r"\[([.#]+)\]", line).group(1)
        lights_goal = np.array([c == "#" for c in pattern])
        lights_state = np.array([False for c in pattern])
        paren_vals = re.findall(r"\(([^)]+)\)", line)
        buttons = [
            tuple(map(int, p.split(","))) if "," in p else (int(p),)
            for p in paren_vals
        ]
        joltages_vals = re.search(r"\{([^}]+)\}", line).group(1)
        joltages = np.array(list(map(int, joltages_vals.split(","))), dtype=int)
        machines.append((lights_goal, lights_state, buttons, joltages))

    all_shortest = 0
    for lights_goal, lights_state, buttons, joltages in machines:
        queue = deque([(lights_state, set(), 0)])
        while queue:
            current_state, seen_states, button_presses = queue.popleft()
            if np.array_equal(current_state, lights_goal):
                all_shortest += button_presses
                break
            if tuple(current_state) in seen_states:
                continue
            seen_states.add(tuple(current_state))
            for button in buttons:
                new_state = current_state.copy()
                new_state[list(button)] = ~new_state[list(button)]
                queue.append((new_state, seen_states, button_presses+1))
    print(all_shortest)


    all_shortest = 0
    for _, _, buttons, joltage_goal in tqdm(machines):
        button_vectors = []
        for button in buttons:
            vec = np.zeros(joltage_goal.shape, dtype=int)
            vec[list(button)] += 1
            button_vectors.append(vec)
        vectors = button_vectors
        b = joltage_goal

        num_vectors = len(vectors)
        dim = len(b)

        problem = pulp.LpProblem(sense=pulp.LpMinimize)
        factors = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(num_vectors)]
        problem += pulp.lpSum(factors)
        for i in range(dim):
            problem += pulp.lpSum(vectors[j][i] * factors[j] for j in range(num_vectors)) == b[i]

        problem.solve(pulp.PULP_CBC_CMD(msg=False))

        factors = [int(var.value()) for var in factors]
        all_shortest += sum(factors)
    print(all_shortest)

if __name__ == '__main__':
    do_main(False)