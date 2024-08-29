def insertion_sort(arr):
    # Traverse array starting from second element
    for i in range(1, len(arr)):
        # Store the current element in a key variable
        key = arr[i]

        # Initialize the position to compare with the sorted portion of the array
        j = i - 1

        # Move elements of the sorted portion that are greater than the key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1  # Exit loop if we go beyond beginning of array

        # Insert the key element in its correct position
        arr[j + 1] = key 

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

    # heap_sort(arr)
    insertion_sort(arr)

    print("\nSorted array is")
    print_array(arr)