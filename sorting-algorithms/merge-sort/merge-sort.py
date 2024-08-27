# Helper function for merging sorted subarrays
def merge(left, right):
    # Result array to store merged values
    result = []

    # Initialize array pointers for left and right subarrays at 0
    i = j = 0

    # Iterate over subarrays to compare elements & append to result in ascending order
    # Exit loop once we've completely iterated over the left or right subarray
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append extra elements (if there are any) to the result array
    # This is necessary in case we have an odd number of total elements in left & right subarrays
    # e.g. merge([4], [5, 6])
    result.extend(left[i:])
    result.extend(right[j:])

    # Return the merged values
    return result

# Recursive function for applying merge_sort algorithm to an array
def merge_sort(arr):
    # Base case for recursion: length of arr == 1 or 0
    if len(arr) <= 1:
        return arr;

    # Determine middle index for splitting into smaller subarrays
    mid = len(arr) // 2

    # Create temp arrays for storing left and right values
    left = arr[:mid]
    right = arr[mid:]

    # Sorted left and right subarrays
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Merge sorted left and right subarrays as we move up the recursive call stack
    return merge(sorted_left, sorted_right)

# Helper function for printing arrays to console
def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]    # Change this array to try sorting different arrays
    print("Given array is")
    print_list(arr)

    sorted = merge_sort(arr)

    print("\nSorted array is")
    print_list(sorted)