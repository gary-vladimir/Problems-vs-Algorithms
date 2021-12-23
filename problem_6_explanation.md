## Max and Min in a Unsorted Array

> In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max

## Solution Explanation

The firs thing I did was to check for invalid input

```python
if len(arr) < 1:
    raise Exception("invalid input")
```

Then, I created two variables, `min_num` and `max_num` that are going to save our results.

```python
min_num = arr[0]
max_num = arr[0]
```

Next, we iterated the array using linear time and we check if we have a new max_num or a new min_num

```python
for num in arr:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
```

Finally, return both variables

```python
return min_num, max_num
```

## Run-time Analysis

The time complexity for this program is: `O(n)`

The space complexity for this program is: `O(1)`
