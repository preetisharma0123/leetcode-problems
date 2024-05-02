# BFS Implementation 1

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def shortest_path(root, target):
    if root == target:
        return 0

    queue = deque([(root, 0)])  # Store tuples of (node, steps)
    visited = set()  # Store visited nodes
    visited.add(root)

    while queue:
        node, steps = queue.popleft()
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                if neighbor == target:
                    return steps + 1
                queue.append((neighbor, steps + 1))
                visited.add(neighbor)

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



