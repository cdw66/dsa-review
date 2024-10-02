def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Iterate while the search space is valid
    while low <= high:
        mid = (low + high) // 2  # Find the middle element

        # If target is found, return the index
        if arr[mid] == target:
            return mid
        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
        # If the target is smaller, ignore the right half
        else:
            high = mid - 1

    return -1  # Target not found

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2  # Find the middle element

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)  # Search in the right half
    else:
        return binary_search_recursive(arr, target, low, mid - 1)  # Search in the left half

# Example usage
if __name__ == "__main__":
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23

    result = binary_search(arr, target)

    # Uncomment to test binary_search_recursive
    # result = binary_search_recursive(arr, target, 0, len(arr) - 1)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")