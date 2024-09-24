# Helper function to perform Counting Sort based on specific digit (exp)
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n    # Output array to store sorted numbers based on current digit
    count = [0] * 10    # Count array to store count of each digit

    # Count occurrences of each digit in given position (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10    # Extract digit at current place value
        count[index] += 1   # Increment digit count

    # Update count array so it contains actual positions of digits in output
    for i in range(1, 10):
        count[i] += count[i - 1]    # Adjust count[i] to hold the actual position in output array

    # Build the output array by placing elements in their correct positions
    for i in range(n - 1, -1, -1):  # Traverse array in reverse order to maintain stability
        index = (arr[i] // exp) % 10    # Get digit at current place value
        output[count[index] - 1] = arr[i]   # Place element at correct position in output array
        count[index] -= 1   # Decrease count for digit

    # Copy output array into original array
    for i in range(n):
        arr[i] = output[i]

# Main function to implement Radix Sort
def radix_sort(arr):
    # Find max number to get number of digits
    max_num = max(arr)

    # Perform Counting Sort for every digit
    exp = 1     # exp is current digit's place value (1 = units, 10 = tens, 100 = hundreds, etc.)
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10   # Move to next significant digit

if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    
    radix_sort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")