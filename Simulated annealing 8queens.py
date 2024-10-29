import random
import math

def count_attacking_pairs(positions):
    attacks = 0
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            if positions[i] == positions[j] or abs(positions[i] - positions[j]) == j - i:
                attacks += 1
    return attacks

def simulated_annealing(n=8, initial_temp=100, cooling_rate=0.95, max_iters=10000):
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_attacks = count_attacking_pairs(current_state)
    temperature = initial_temp

    for _ in range(max_iters):
        if current_attacks == 0:
            break
        next_state = current_state[:]
        col = random.randint(0, n - 1)
        new_row = random.randint(0, n - 1)
        next_state[col] = new_row
        next_attacks = count_attacking_pairs(next_state)
        delta_e = current_attacks - next_attacks

        if delta_e > 0 or random.uniform(0, 1) < math.exp(delta_e / temperature):
            current_state, current_attacks = next_state, next_attacks

        temperature *= cooling_rate

    return current_state, current_attacks

solution, attacks = simulated_annealing()
if attacks == 0:
    print("Solution found:")
    print("Queen positions by column:", solution)
else:
    print("No perfect solution found. Closest configuration:")
    print("Queen positions by column:", solution)
    print("Remaining attacking pairs:", attacks)
