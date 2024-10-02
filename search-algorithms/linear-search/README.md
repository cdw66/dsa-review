# Linear Search

**Linear Search** is the simplest searching algorithm that checks each element in a list or array sequentially until the desired element is found or the entire list has been checked. It is often used for small or unsorted data, and it works for any type of list or array.

**Linear Search** uses the following steps to search for elements in an array:

1. **Start at First Element**: Begin by examining the first element of the list/array.
2. **Move to Next Element & Compare**: If the previous element was not equal to the target element, move on to the next element and compare.
3. **Repeat**: Repeat this process, visiting every element in the array until either the target element is found or you reach the end of the array.
4. **Return Result**: If the target value is found, return its position (index) of the list. Otherwise, return a failure indicatior (usually `-1`, `None`, or `False`).

## Time & Space Complexity

| Complexity       | Best Case | Average Case | Worst Case |
| ---------------- | --------- | ------------ | ---------- |
| Time Complexity  | $O(1)$    | $O(n)$       | $O(n)$     |
| Space Complexity | $O(1)$    | -            | -          |

### Explanation

- **Time Complexity**: **Linear Search** has a best case time complexity of $O(1)$ if the first element is the target value and average & worst case complexity of $O(n)$, since the algorithm needs to check every element in the list.
- **Space Complexity**: **Linear Search** has a constant space complexity of $O(1)$, since it does not need any additional storage beyond the input list.

## Example

Let's use **Linear Search** to find the element `7` in the array `arr = [3, 8, 1, 7, 9, 2]`.

### First Element

Compare the first element `3` with the target element `7` - Not a match, move on to the next element.

### Second Element

Compare the next element `8` with `7` - Not a match, move on to the next element.

### Third Element

Compare the next element `1` with `7` - Not a match, move on to the next element.

### Fourth Element

Compare the next element `7` with `7` - Match found, stop iterating and return the current index, `3`.

In this example, **Linear Search** returns `3`, because we found it at position `arr[3]`.

## Implementation (Python)

```python
def linear_search(arr, target):
    # Traverse through the list or array
    for i in range(len(arr)):
        # Check if the current element matches the target
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not found
```

## Characteristics of Linear Search

1. **Simple & Easy to Implement**: **Linear Search** is one of the simplest search algorithm and can be implemented very easily using a `for` loop.

2. **Works on Unsorted Data**: **Linear Search** can be applied to any data structure that allows sequential access, regardless of whether or not the data is sorted.

3. **Inefficient for Large Arrays**: The time complexity of $O(n)$ makes **Linear Search** inefficient for large arrays. It is best used on small lists or arrays or when more efficient search algorithms are not applicable.

4. **Sequential Access**: **Linear Search** works by sequentially accessing each element in the array or list, making it straightforward but less efficient than other search algorithms.

## References

- [Geeks for Geeks Introduction to Linear Search Algorithm](https://www.geeksforgeeks.org/linear-search/)
