# Quick Sort

**Quick Sort** is a highly-efficient sorting algorithm that uses the divide-and-conquer approach to sort elements. Unlike **Merge Sort**, which divides the array into halves, Quick Sort works by selecting a "pivot" element and partitioning the array around this pivot, placing elements less than the pivot to its left and elements greater than the pivot to its right. This partitioning process is repeated recursively on each subarray until the entire array is sorted.

Here are the steps that **Quick Sort** follows to sort an array:

1. **Choose Pivot**: Select an element as a pivot. The pivot can be chosen in many ways (e.g., the first element, the last element, a random element, or the median of three).
2. **Partition**: Rearrange the array such that all elements less than the pivot are to its left, and all elements greater than the pivot are to its right.
3. **Recursively Apply**: Recursively apply the same steps to the left and right subarrays created by the partition. Combine the results by concatenating the sorted subarrays around the pivot to produce the final sorted array.

## Time & Space Complexity

| Complexity       | Best Case      | Average Case   | Worst Case |
| ---------------- | -------------- | -------------- | ---------- |
| Time Complexity  | $O(n\ log(n))$ | $O(n\ log(n))$ | $O(n^2)$   |
| Space Complexity | $O(log(n))$    | $O(log(n))$    | $O(n)$     |

### Explanation

- Time Complexity

  - **Best and Average Case**: $O(n\ log(n))$, when the pivot divides the array into two relatively equal parts.
  - **Worst Case**: $O(n^2)$, when the pivot results in highly unbalanced partitions (e.g., always the smallest or largest element).

- Space Complexity
  - **Best and Average Case**: $O(log(n))$, due to the recursive call stack depth.
  - **Worst Case**: $O(n)$, when recursion depth reaches $n$ in cases of highly unbalanced partitions (like a sorted array).

## Example

In this example, we'll use **Quick Sort** to sort the following array: `arr = [10, 80, 30, 90, 40]`. Note that we are choosing the last element as the pivot at each step in this case.

### 1. Initial Call & Partition

With the input array `arr = [10, 80, 30, 90, 40]`, on our first call to `quick_sort()`, we choose the last element, `40`, as our pivot. We then partition the array so that elements less than `40` are on its left, and elements greater than `40` are on its right. After partitioning, we swap the pivot into its correct position, resulting in the array `[10, 30, 40, 90, 80]`. The pivot `40` is now in its sorted position `arr[2]`. We then recursively call `quick_sort()` on the left subarray `[10, 30]` and the right subarray `[90, 80]`.

### 2. First Recursive Call

Repeating the process from the last step for our two partitions:

#### Lesser Partition (`quick_sort([10, 30])`)

- The pivot is `30` (last element).
- The subarray `[10, 30]` is already sorted (as both `10` and `30` are in their correct positions relative to each other and the pivot `30`).
- No further partitioning is needed since the subarray `[10, 30]` has only two elements.
- Recursively calling quick_sort on the partitions created in this step (`[10]` and `[]`) will trigger the base case since these are either single-element or empty subarrays.

#### Greater Partition (`quick_sort([90, 80])`)

- The pivot is `80` (last element).
- During partitioning, `90` and `80` are compared. Since `90 > 80`, we swap `90` and `80` to get `[80, 90]`.
- The pivot `80` is now in its correct sorted position (`arr[3]`).
- Recursively calling `quick_sort()` on `[]` and `[90]` will trigger the base case since these are either single-element or empty subarrays.

### 3. Second Recursive Call (Base Case)

Calling `quick_sort()` on the single-element and empty partitions created in the last step triggers our base case (`low >= high`), so the function returns immediately. As each recursive call reaches its base case and returns, we begin moving back up the call stack, combining the sorted subarrays until the entire array is sorted. The final sorted array is `[10, 30, 40, 80, 90]`.

## Implementation (Python)

```python
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
```

## Key Points

### When to Use Quick Sort

- **Average-Case Performance**: **Quick Sort** is generally preferred when you expect average-case performance of $O(n\ log(n))$ due to its efficient in-place sorting and relatively low overhead. It often performs better in practice than other $O(n\ log(n))$ algorithms like **Merge Sort** due to fewer data movements and better cache performance.

- **In-Place Sorting**: Use **Quick Sort** when space efficiency is crucial. Unlike **Merge Sort**, which requires $O(n)$ additional space for merging, **Quick Sort** operates in place with $O(log(n))$ space complexity due to the recursive stack. This makes it ideal for large datasets where minimizing memory usage is important.

- **When Data Fits in Memory**: **Quick Sort** is an excellent choice when all data fits in memory, as it minimizes memory usage and benefits from efficient data access patterns.

- **When You Can Choose a Good Pivot**: **Quick Sort** performs exceptionally well when you can choose a good pivot that splits the array into two nearly equal parts. This minimizes the depth of the recursion and optimizes performance.

### When Not to Use Quick Sort

- **Worst-Case Scenarios**: Avoid using **Quick Sort** on datasets that are nearly sorted or contain many duplicate elements, especially if a naive pivot selection strategy is used (e.g., always picking the first or last element as the pivot). These scenarios can lead to the worst-case time complexity of $O(n^2)$.

- **Stability Requirements**: **Quick Sort** is not a stable sorting algorithm, meaning that it does not preserve the relative order of equal elements. If stability is a requirement (e.g., when sorting records by multiple fields), consider using a stable sort like **Merge Sort** or **Timsort** (used in Python's built-in `sorted()` function).

- **Small Datasets**: For very small datasets (e.g., fewer than 10 elements), simpler algorithms like **Insertion Sort** may perform better due to their lower overhead and simpler implementation. In practice, a hybrid approach like introspective sort (**Introsort**) combines **Quick Sort** with **Insertion Sort** for small partitions.

- **Highly Recursive Environments**: Avoid using **Quick Sort** in environments with limited stack space or where deep recursion can lead to stack overflow, especially with large datasets. For such cases, consider using an iterative version of **Quick Sort** or another algorithm with better stack usage characteristics.

### Handy Tips for Quick Sort

- **Choosing a Good Pivot**: The efficiency of **Quick Sort** heavily depends on the choice of pivot. Common strategies include:

  - **Random Pivot**: Choose a pivot randomly to reduce the likelihood of hitting the worst case on already sorted or nearly sorted data.
  - **Median-of-Three**: Choose the median of the first, middle, and last elements as the pivot. This strategy often provides a good balance and reduces the chance of worst-case performance.

- **Tail Recursion Optimization**: Implement [tail call optimization](https://stackoverflow.com/questions/310974/what-is-tail-call-optimization) (TCO) where possible to reduce the stack depth and prevent stack overflow in languages or environments that support it. This involves always recursing into the smaller partition first.

- **Hybrid Sorting**: Consider using a hybrid sorting approach that switches to a simpler algorithm like **Insertion Sort** for small subarrays. This can optimize **Quick Sort**'s performance by reducing recursive overhead for small partitions.

- **Iterative Implementation**: For environments where recursion depth is a concern, consider implementing an iterative version of **Quick Sort** using a stack data structure to manage subarray indices.

- **Avoiding Worst Case**: To avoid the worst-case time complexity, choose a good pivot and apply randomization or shuffle the array before sorting.

- **Parallel Quick Sort**: **Quick Sort** is well-suited for parallelization, especially when applied to large datasets. Partitioning can be parallelized by sorting the two halves concurrently on different processors or threads, significantly improving performance on multi-core systems.

- **Handling Duplicate Elements**: If your dataset contains many duplicate elements, consider modifying the partitioning strategy to handle equal elements more efficiently, such as using the three-way partitioning ([Dutch National Flag problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)) to partition elements into three groups: less than, equal to, and greater than the pivot.

- **Understand Algorithm Limitations**: Recognize that while **Quick Sort** is fast in practice, its performance can degrade significantly in certain scenarios. It is essential to understand the input characteristics and choose the appropriate sorting algorithm based on those characteristics.

## References

- [Geeks for Geeks Quick Sort Algorithm](https://www.geeksforgeeks.org/quick-sort-algorithm/)
