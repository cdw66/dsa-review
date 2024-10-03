from collections import deque

# ----------------- TREE BFS (Level-order Traversal) ----------------- #

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BFS for Tree (Level-order Traversal)
def bfs_tree(root):
    if root is None:
        return

    queue = deque([root]) # Initialize queue with root node

    while queue:
        node = queue.popleft() # Process the first node (FIFO)
        print(node.value, end=' ')

        # Enqueue the left child
        if node.left:
            queue.append(node.left)

        # Enqueue the right child
        if node.right:
            queue.append(node.right)


# ----------------- GRAPH BFS (Traversal) ----------------- #

# BFS for Graphs
def bfs_graph(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize queue with the start node

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            # Enqueue all unvisited neighbors of the current node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# ----------------- MAIN EXECUTION ----------------- #

def main():
    # TREE EXAMPLE:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("BFS (Level-order Traversal) of Tree:")
    bfs_tree(root)  # Output: 1 2 3 4 5
    print("\n")

    # GRAPH EXAMPLE:
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3]
    }

    print("BFS Traversal of Graph:")
    bfs_graph(graph, 0)  # Output: 0 1 2 3 4


# Call the main function to execute the BFS examples
if __name__ == "__main__":
    main()
