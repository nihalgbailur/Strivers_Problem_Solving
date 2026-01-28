# DSA Practice — Final Notes (2 Questions)

## 1) Largest Element

**Problem:** Given an array of integers `nums`, return the value of the **largest** element.

### Optimal Idea (One-pass scan)
- Keep a variable `max_val` starting at the first element.
- Scan the array and update `max_val` whenever you find a bigger number.

### Time / Space
- **Time:** `O(n)`  
- **Space:** `O(1)`

### Final Answer (Python)
```python
class Solution:
    def largestElement(self, nums):
        max_val = nums[0]
        for x in nums[1:]:
            if x > max_val:
                max_val = x
        return max_val
```

---

## 2) Check if the Array is Sorted II

**Problem:** Given an array `nums` of length `n`, return `True` if the array is sorted in **non-decreasing** order, else return `False`.

**Non-decreasing** means: `nums[i-1] <= nums[i]` for every valid `i`.

### Optimal Idea (Adjacent check)
- Walk through the array from index `1` to `n-1`.
- If you ever find `nums[i] < nums[i-1]`, it breaks the non-decreasing rule → return `False`.
- If the loop completes, return `True`.

### Time / Space
- **Time:** `O(n)`  
- **Space:** `O(1)`

### Final Answer (Python)
```python
class Solution:
    def isSorted(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True
```
