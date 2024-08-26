def bubbleSort(arr):
    n = len(arr)

    # Traverse array elements
    for i in range(n):
        swapped = False

        # Last i elements are already sorted
        for j in range(0, n-i-1):

            # Traverse array from 0 to end of unsorted elements (n-i-1)
            # Swap elements if element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap elements
                swapped = True

            # Break out of loop if elements are in order
            if (swapped == False):
                break

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")