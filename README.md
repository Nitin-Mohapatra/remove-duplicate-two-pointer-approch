# Remove Element using Two Pointer Approach

## Problem
Given an array and a target value, remove all occurrences of the target **in-place** and return the new length of the array.

---

## Problem Keywords
- Remove Element LeetCode Solution  
- Two Pointer Approach in Arrays  
- Remove Target Element from Array in-place  
- Python Array In-place Modification  
- Array Filtering without Extra Space

---

## Code
```python
arr = [0,1,2,2,3,0,4,2]
target = 2
j = 0

for i in range(len(arr)):
    if arr[i] != target:
        arr[j] = arr[i]
        j += 1

print(arr[:j])   # Output: [0, 1, 3, 0, 4]


## Approach (Two Pointer)

- Take **two pointers**:
  - `i` → scans the entire array  
  - `j` → tracks where the next non-target element should be placed  

- For each element:
  - If `arr[i] != target`:  
    - Place it at `arr[j]`  
    - Increment `j` (since we filled that position)  
  - If `arr[i] == target`:  
    - Skip it (do nothing)  

- After the loop, the first `j` elements in `arr` will be the result array (without target).  
