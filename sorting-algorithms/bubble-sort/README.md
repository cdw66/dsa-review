# Bubble Sort

_Bubble Sort_ is a simple sorting algorithm that works by swapping adjacent elements if they are in the wrong order. The algorithm performs multiple passes over the array, building up a partition of sorted elements at the end of the array, until all of the elements are in order. In this way, the largest elements "bubble" their way up to the end of the array, which is how _Bubble Sort_ gets its name.

This makes _Bubble Sort_ inefficient at sorting large datasets, but it is easy to understand and implement.

## Time & Space Complexity

| Complexity       | Big O Notation |
| ---------------- | -------------- |
| Time Complexity  | O(n^2^)        |
| Space Complexity | O(1)           |

## Example

Let's use _Bubble Sort_ to sort the following array: `[14, 8, 11, 2]`

### First Iteration

Given the input array `arr = [14, 8, 11, 2]`, we start by comparing the first two elements: `[|14, 8|, 11, 2]`. Since `14` is greater than `8`, we swap the elements to get `[8, 14, 11, 2]`.

Next, we move forward one index in the array to compare the next two elements: `[8, |14, 11|, 2]`. Since we swapped `14` into the second position (`arr[1]`), we now compare `14` and `11`. `14` is greater than `11`, so again, we swap the two elements to get the array `[8, 11, 14, 2]`.

Moving forward in the array again, we compare the next two elements: `[8, 11, |14, 2|]`. `14` is greater than `2`, so we swap the elements. Now, our array is `[8, 11, 2, 14]`. Notice how the greatest element in our array, `14`, has "bubbled up" to the end of the array.

### Second Iteration

Our elements are still not sorted, so we need to perform another pass on the array. Starting with `[8, 11, 2, 14]`, we compare the first two elements: `[|8, 11|, 2, 14]`. `8` is less than `11`, so in this case, we move on to the next pair of values in the array without swapping any values.

Next, we move forward in the array and compare the elements: `[8, |11, 2|, 14]`. `11` is greater than `2`, so we swap the elements to get `[8, 2, 11, 14]`.

Since we know that the last `n-i-1` elements of the array are in order, we can stop here for this iteration.

### Third Iteration

Our array is almost sorted, so let's perform another pass. Starting with `[8, 2, 11, 14]`, we compare the first two elements: `[|8, 2|, 11, 14]`. `8` is greater than `2`, so we swap the elements to get `[2, 8, 11, 14]`. Since we already know the last `i` elements are sorted, we can stop here for this iteration. Our array is now in order, but _Bubble Sort_ will still perform one final pass.

### Fourth Iteration

With our array sorted like this: `[2, 8, 11, 14]`, _Bubble Sort_ performs one final pass to ensure our elements are in order. We start by comparing the first two elements again: `[|2, 8|, 11, 14]`. Since `2` is less than `8`, our loop exits and the _Bubble Sort_ is complete. Now, `arr = [2, 8, 11, 14]`.

## Implementation (Python)

```
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
```

## References

- [GeeksForGeeks Bubble Sort Algorithm](https://www.geeksforgeeks.org/bubble-sort-algorithm/)
