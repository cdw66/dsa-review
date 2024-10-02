def linear_search(arr, target):
    # Traverse through the list or array
    for i in range(len(arr)):
        # Check if the current element matches the target
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [3, 8, 1, 7, 9, 2]
target = 7
result = linear_search(arr, target)

if __name__ == "__main__":
    arr = [3, 8, 1, 7, 9, 2]
    target = 7
    
    result = linear_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")