import random
import math

N = 8

def calculate_cost(board):
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                cost += 1
    return cost

def generate_initial_solution():
    return [random.randint(0, N - 1) for _ in range(N)]

def get_neighbor(board):
    new_board = board[:]
    col = random.randint(0, N - 1)
    row = random.randint(0, N - 1)
    new_board[col] = row
    return new_board

def simulated_annealing():
    current_solution = generate_initial_solution()
    current_cost = calculate_cost(current_solution)
    
    initial_temperature = 1000
    final_temperature = 0.1
    cooling_rate = 0.995
    max_iterations = 10000

    temperature = initial_temperature
    iterations = 0

    while temperature > final_temperature and iterations < max_iterations:
        neighbor_solution = get_neighbor(current_solution)
        neighbor_cost = calculate_cost(neighbor_solution)
        
        if neighbor_cost < current_cost:
            current_solution = neighbor_solution
            current_cost = neighbor_cost
        else:
            probability = math.exp((current_cost - neighbor_cost) / temperature)
            if random.random() < probability:
                current_solution = neighbor_solution
                current_cost = neighbor_cost
        
        temperature *= cooling_rate
        iterations += 1
        
        if current_cost == 0:
            break
    
    return current_solution, current_cost

solution, cost = simulated_annealing()

if cost == 0:
    print("Solution found:")
    for row in range(N):
        board = ['Q' if col == solution[row] else '.' for col in range(N)]
        print(" ".join(board))
else:
    print("No solution found within the iteration limit.")
