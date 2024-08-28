# Helper function for heapifying subtree rooted at index i
# n is the size of the heap
def heapify(arr, n, i):
    # Assume the largest element is the root
    largest = i

    left = 2 * i + 1    # Root's left child index
    right = 2 * i + 2   # Root's right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest element is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        # We need to call heapify again on the subtree to ensure that it does not violate max tree properties
        # It is possible that after being swapped, one of the node's children is still greater than it
        heapify(arr, n, largest)

# Main heap sort function
def heap_sort(arr):
    n = len(arr)

    # Step 1. Build the Max Heap
    # ------------------------------------
    # The node at index (n // 2 - 1) is the index of the last non-leaf node in the heap
    # The nodes at indices (n * i + 1) and (n * i + 2) are its left and right children (leaf nodes), respectively
    #
    # This loop iterates in reverse (from bottom to top of the heap) over all non-leaf nodes in the tree and heapifies them
    #
    # Iterating over non-leaf nodes in reverse is most efficient, because it ensures that when we call `heapify()` on a node, its subtree is already a valid heap
    #
    # This also ensures that the largest nodes are correctly moved to the top of their subtree, and eventually to the top of the heap    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2. Extract Elements from the Heap One by One
    for i in range(n - 1, 0, -1):
        # Move current root (largest element) to the end of the array
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap to maintain max heap property
        # Note: We call heapify with n = i, reducing the size of the heap (i.e., skipping the sorted elements at the end of the array)
        heapify(arr, i, 0)

# Function to print an array
def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]   # Change this array to try sorting different arrays
    print("Given array is")
    print_array(arr)

    heap_sort(arr)

    print("\nSorted array is")
    print_array(arr)