# Search in a Rotated Sorted Array

> You are given a target value to search. If found in the array return its index, otherwise return -1.

## Solution Explanation

The firs thing I did was to check for invalid cases, that is, if the passed array it's empty or it only has one element and it's not the target

```python
size = len(input_list)
if size == 0 or (size == 1 and input_list[0] != number):
    return -1
```

If none of those conditions are True, then proceed to do a binary search:

```python
left, right = 0, size-1
while left <= right:
    mid = (left + right)//2
    if input_list[mid] == number:
        return mid
    if input_list[left] <= input_list[mid]:
        if input_list[left] <= number < input_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if input_list[mid] < number <= input_list[right]:
            left = mid + 1
        else:
            right = mid - 1
return -1
```

## Run-time Analysis

The time complexity of this program is: `O(logn)`

The space complexity for this program is: `O(1)` because it does not use recursion
