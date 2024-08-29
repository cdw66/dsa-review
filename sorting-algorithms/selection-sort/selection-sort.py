def selection_sort(arr):
    # Traverse the entire array
    for i in range(len(arr)):
        # Assume current element is the minimum
        mindex = i

        # Find the minimum element in the remaining unsorted partition
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mindex]:
                mindex = j

    # Swap the found minimum element with the first element of the unsorted portion
    arr[i], arr[mindex] = arr[mindex], arr[i]

