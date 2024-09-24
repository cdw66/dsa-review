# Radix Sort

**Radix Sort** is a non-comparison-based sorting algorithm that sorts numbers by processing their individual digits. Instead of comparing elements directly like most sorting algorithms, **Radix Sort** sorts numbers digit by digit, starting from the least significant digit (LSD) to the most significant digit (MSD). This approach is especially efficient when sorting large lists of numbers with a similar number of digits.

The steps of **Radix Sort** can be summarized like this:

1. **Find the Maximum Element**: Find the number with the most digits in the array. This will determine how many iterations are required to process all the digits.
2. **Sort by Each Digit**: Starting from the LSD (the rightmost digit), group the numbers based on this digit. For each digit, use a stable sorting algorithm to ensure the order of numbers with the same digit is preserved.
3. **Move to the Next Significant Digit**: Once the numbers are sorted by the current digit, move to the next significant digit (the next digit to the left), and repeat the process.
4. **Repeat Until All Digits are Processed**: Continue sorting digit by digit until you've processed the most significant digit.

## Time & Space Complexity

| Complexity       | Big O Notation |
| ---------------- | -------------- |
| Time Complexity  | $O(d*(n+k))$   |
| Space Complexity | $O(n+k)$       |

### Explanation

- **Time Complexity**: The time complexity depends on $d$, the number of digits in the largest number, and $n$, the number of elements. The factor $k$ represents the range of digits (0-9 for decimal numbers). In practice, **Radix Sort** is $O(n)$ when sorting fixed-length integers. In other words, each pass of **Radix Sort** takes $O(n+k)$ time, and since we must perform $d$ passes, the total time complexity is $O(d*(n+k))$.
- **Space Complexity**: **Radix Sort** requires extra space proportional to the input size ($n$) and the range of digits ($k$).

## Example

Let's use **Radix Sort** to sort the array `arr = [170, 45, 75, 90, 802, 24, 2, 66]`.

### Step 1: Find Largest Element in `arr`

Find the largest element in the array, which is `802`. It has three digits, so we will perform three passes of **Radix Sort**, one pass for each significant digit.

### Step 2: Sort by Unit Place Digits

Sort the elements based on the LSD (the unit place) using a stable sorting technique, such as **Counting Sort**. Note that the default implementation of **Counting Sort** is unstable, but we can solve this problem by iterating over `arr` in reverse order to build the output array. This allows us to keep the keys in the same order as they appear in `arr`.

After performing **Counting Sort** on the unit place digits, the resulting array is `[170, 90, 802, 2, 24, 45, 75, 66]`.

![]()

### Step 3: Sort by Tens Place Digits

Next, we perform **Counting Sort** on the tens place digits. The resulting array from this operation is `[802, 2, 24, 45, 66, 170, 75, 90]`.

**Note**: Elements that don't have a number in the tens place use `0` as a placeholder, e.g. the element `2` should be treated as `02`.

![]()

### Step 4: Sort by Hundreds Place Digits

Finally, we perform the final pass of **Counting Sort** on the hundreds place digits to obtain the sorted array. The final sorted array is `[2, 24, 45, 66, 75, 90, 170, 802]`.

![]()
