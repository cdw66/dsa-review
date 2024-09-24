def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    
    # Initialize count array with size max_val + 1
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element
    for num in arr:
        count[num] += 1

    # Accumulate the count array 
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):  # Traverse input array in reverse to maintain stability
        output[count[num] - 1] = num
        count[num] -= 1

    # Copy the sorted elements back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]

# Example usage
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    
    counting_sort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
