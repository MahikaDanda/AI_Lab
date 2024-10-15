import heapq

def misplaced_tiles(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j] and state[i][j] != 0:
                count += 1
    return count

def get_empty_tile_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_new_states(state):
    i, j = get_empty_tile_position(state)
    possible_moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    for di, dj in directions:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            possible_moves.append(new_state)
    return possible_moves

def print_puzzle(state):
    for row in state:
        print(' '.join(str(x) if x != 0 else '_' for x in row))
    print()

def a_star(start, goal):
    queue = []
    heapq.heappush(queue, (misplaced_tiles(start, goal), 0, start, []))

    visited = set()
    visited.add(tuple(tuple(row) for row in start))

    while queue:
        f, g, current_state, path = heapq.heappop(queue)
        print(f"Step {g}:")
        print(f"g(n) = {g}, h(n) = {f - g}")
        print("Current puzzle state:")
        print_puzzle(current_state)

        if current_state == goal:
            print("Goal state reached!")
            print(f"Total moves: {g}")
            print("Solution path:")
            for step, state in enumerate(path + [current_state], 1):
                print(f"Move {step}:")
                print_puzzle(state)
            return

        print("Generated new states (possible moves):")
        trial_states = []
        for new_state in generate_new_states(current_state):
            if tuple(tuple(row) for row in new_state) not in visited:
                h = misplaced_tiles(new_state, goal)
                trial_states.append((g + h + 1, g + 1, new_state, h))
                print(f"g(n) = {g + 1}, h(n) = {h}")
                print_puzzle(new_state)

        print("Evaluating and choosing the best state based on f(n):")
        for f_new, g_new, state, h_new in trial_states:
            if tuple(tuple(row) for row in state) not in visited:
                heapq.heappush(queue, (f_new, g_new, state, path + [current_state]))
                visited.add(tuple(tuple(row) for row in state))
                print(f"Chosen state with f(n) = {f_new} (g(n) = {g_new}, h(n) = {h_new}):")
                print_puzzle(state)

    print("No solution found")
    return

start_state = [[2, 8, 3],
               [1, 6, 4],
               [0,7, 5]]

goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]  

a_star(start_state, goal_state)
