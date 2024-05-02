# BFS Implementation 2

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def shortest_path(root, target):
    if root == target:
        return 0

    queue = deque([root])  # Store nodes waiting to be processed
    visited = set()  # Store visited nodes
    visited.add(root)
    step = 0  # Number of steps needed from root to current node

    while queue:
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            if cur == target:
                return step
            for next_node in cur.neighbors:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.add(next_node)
        step += 1

    return -1  # No path found

# Example usage:
# Define nodes and build the graph
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
root.neighbors = [node2, node3]
node2.neighbors = [root, node4]
node3.neighbors = [root]
node4.neighbors = [node2]

# Call the function to find the shortest path
target = node4
print(shortest_path(root, target))  # Output: 2
