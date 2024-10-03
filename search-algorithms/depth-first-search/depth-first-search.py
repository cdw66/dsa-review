class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ----------------- TREE TRAVERSALS (DFS) ----------------- #

# Recursive DFS (Pre-order Traversal)
def dfs_preorder_recursive(node):
    if node is None:
        return

    # Visit the root
    print(node.value, end=' ')

    # Recursively visit the left subtree
    dfs_preorder_recursive(node.left)

    # Recursively visit the right subtree
    dfs_preorder_recursive(node.right)


# Recursive DFS (In-order Traversal)
def dfs_inorder_recursive(node):
    if node is None:
        return

    # Recursively visit the left subtree
    dfs_inorder_recursive(node.left)

    # Visit the root
    print(node.value, end=' ')

    # Recursively visit the right subtree
    dfs_inorder_recursive(node.right)


# Recursive DFS (Post-order Traversal)
def dfs_postorder_recursive(node):
    if node is None:
        return

    # Recursively visit the left subtree
    dfs_postorder_recursive(node.left)

    # Recursively visit the right subtree
    dfs_postorder_recursive(node.right)

    # Visit the root
    print(node.value, end=' ')


# Iterative DFS (Pre-order Traversal)
def dfs_preorder_iterative(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.value, end=' ')

        # Push right child first, so that left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Iterative DFS (In-order Traversal)
def dfs_inorder_iterative(root):
    if root is None:
        return

    stack = []
    current = root

    while current is not None or stack:
        # Reach the leftmost node of the current node
        while current is not None:
            stack.append(current)
            current = current.left

        # Current is None, so we pop the top element
        current = stack.pop()
        print(current.value, end=' ')

        # We now visit the right subtree
        current = current.right


# Iterative DFS (Post-order Traversal)
def dfs_postorder_iterative(root):
    if root is None:
        return

    stack = []
    result = []  # Use a result list to store the post-order sequence
    stack.append(root)

    while stack:
        node = stack.pop()
        result.append(node.value)

        # Push left child first, so that right is processed first
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # The result is in reverse post-order, so we reverse it before printing
    print(' '.join(map(str, result[::-1])))


# ----------------- GRAPH TRAVERSALS (DFS) ----------------- #

# Recursive DFS for Graphs
def dfs_recursive_graph(graph, node, visited=None):
    if visited is None:
        visited = set()

    # Mark the node as visited
    visited.add(node)
    print(node, end=' ')

    # Explore each adjacent node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive_graph(graph, neighbor, visited)


# Iterative DFS for Graphs
def dfs_iterative_graph(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            # Add neighbors to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


# ----------------- MAIN EXECUTION ----------------- #

def main():
    # TREE EXAMPLE:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Tree Traversal - Pre-order (Recursive):")
    dfs_preorder_recursive(root)  # Output: 1 2 4 5 3
    print("\nTree Traversal - Pre-order (Iterative):")
    dfs_preorder_iterative(root)  # Output: 1 2 4 5 3

    print("\nTree Traversal - In-order (Recursive):")
    dfs_inorder_recursive(root)  # Output: 4 2 5 1 3
    print("\nTree Traversal - In-order (Iterative):")
    dfs_inorder_iterative(root)  # Output: 4 2 5 1 3

    print("\nTree Traversal - Post-order (Recursive):")
    dfs_postorder_recursive(root)  # Output: 4 5 2 3 1
    print("\nTree Traversal - Post-order (Iterative):")
    dfs_postorder_iterative(root)  # Output: 4 5 2 3 1

    print("\n")

    # GRAPH EXAMPLE:
    graph = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [],
        4: []
    }

    print("Graph Traversal - DFS (Recursive):")
    dfs_recursive_graph(graph, 0)  # Output: 0 1 3 2 4
    print("\nGraph Traversal - DFS (Iterative):")
    dfs_iterative_graph(graph, 0)  # Output: 0 1 3 2 4


# Call the main function to execute the examples
if __name__ == "__main__":
    main()
