# Helper function for partitioning subarrays
def partition(arr, low, high):
    # Choose our pivot (the last element of arr)
    pivot = arr[high]

    # This pointer keeps track of our partition between smaller and larger elements
    # i.e. i is the index of the first element larger than the pivot
    i = low - 1

    # Compare other elements in the array to pivot element
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Move "boundary" up

            # Swap elements to put smaller element before partition (i) and larger element after
            arr[i], arr[j] = arr[j], arr[i] 

    # Swap the pivot element with the element at i+1 to place it between the partitions
    arr[i + 1], arr[high] = arr[high], arr[i+1]
    return i + 1    # Return the partitioning index

def quick_sort(arr, low, high):
    # Base case: Stop if arr has <= 1 elements
    if low < high:
        # Partition the array and get pivot index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after pivot index
        quick_sort(arr, low, pi -1)
        quick_sort(arr, pi + 1, high)

# Function to print an array
def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Given array is")
    print_array(arr)

    quick_sort(arr, 0, len(arr)-1)

    print("\nSorted array is")
    print_array(arr)