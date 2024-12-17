 class Node:
    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children if children is not None else []
        self.value = value

def evaluate(node):
    return node.value

def is_terminal(node):
    return node.value is not None

def get_children(node):
    return node.children

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player, path=[]):
    # Terminal condition: leaf node or depth is 0
    if depth == 0 or is_terminal(node):
        return evaluate(node), path

    if maximizing_player:
        max_eval = float('-inf')
        optimal_path = None
        for child in get_children(node):
            child_value, child_path = alpha_beta_pruning(child, depth - 1, alpha, beta, False, path + [child.name])
            if child_value > max_eval:
                max_eval = child_value
                optimal_path = child_path
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval, optimal_path
    else:
        min_eval = float('inf')
        optimal_path = None
        for child in get_children(node):
            child_value, child_path = alpha_beta_pruning(child, depth - 1, alpha, beta, True, path + [child.name])
            if child_value < min_eval:
                min_eval = child_value
                optimal_path = child_path
            beta = min(beta, min_eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval, optimal_path

# Create the game tree
H = Node('H', value=10)
I = Node('I', value=9)
J = Node('J', value=14)
K = Node('K', value=18)
L = Node('L', value=5)
M = Node('M', value=4)
N = Node('N', value=50)
O = Node('O', value=3)

D = Node('D', children=[H, I])
E = Node('E', children=[J, K])
F = Node('F', children=[L, M])
G = Node('G', children=[N, O])

B = Node('B', children=[D, E])
C = Node('C', children=[F, G])

A = Node('A', children=[B, C])

# Run the alpha-beta pruning algorithm
maximizing_player = True
initial_alpha = float('-inf')
initial_beta = float('inf')
depth = 3  # Maximum depth of the tree

optimal_value, optimal_path = alpha_beta_pruning(A, depth, initial_alpha, initial_beta, maximizing_player)
print(f"The optimal value is: {optimal_value}")
print(f"The optimal path is: A -> {' -> '.join(optimal_path)}")
