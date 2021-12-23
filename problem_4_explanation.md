## Dutch National Flag Problem

> Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

## Solution Explanation

The firs thing I did was to create three empty arrays.

```python
zeros, ones, twos = [], [], []
```

Then, iterate through the input_list and for each character check if the num is equal to 0, 1, or 2 and append the num to the correspondent array

```python
for num in input_list:
    if num == 0:
        zeros.append(num)
    elif num == 1:
        ones.append(num)
    elif num == 2:
        twos.append(num)
    else:
        raise Exception("Invalid array input")
```

Finally, add all arrays together

```python
return zeros + ones + twos
```

## Run-time Analysis

The time complexity of this program is: `O(n)`

The space complexity for this program is: `O(3)`
