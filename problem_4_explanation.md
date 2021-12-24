## Dutch National Flag Problem

> Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

## Solution Explanation

The first thing I did, was to check for invalid input

```python
if len(input_list) <= 0:
    return input_list
```

Then, I used the numpy to see how many times an element was present

```python
unique, counts = numpy.unique(numpy.array(input_list), return_counts=True)
zeros = counts[0]
ones = counts[1]
twos = counts[2]
```

Finally, I returned the arrays multiplied by how many times they were present in the correct order

```python
return ([0] * zeros) + ([1] * ones) + ([2] * twos)
```

## Run-time Analysis

The time complexity of this program is: `O(n)`

The space complexity for this program is: `O(1)`
