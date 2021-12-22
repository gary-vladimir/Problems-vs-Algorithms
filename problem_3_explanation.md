# Rearrange Array Elements

> Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

## Solution Explanation

The firs thing I did was to check for invalid cases, that is, if the passed array has a size less than two

```python
size = len(input_list)
if size <= 2:
    return input_list
```

Then, I wrote another file named `Quick_Sort` where I implemented the quicksort algorithm learned in the Udacity lessons and imported it

```python
from Quick_Sort import quicksort
```

Back to our function, I did a quicksort on the input list using the imported algorithm

```python
quicksort(input_list)
```

Finally, I iterated through the sorted list in steps of two starting from the tail of the array and appended the first and second biggest numbers to a first and second string variables

```python
first, second = '', ''
for i in range(size - 1, -1, -2):
    first += str(input_list[i])
    if i - 1 >= 0:
        second += str(input_list[i - 1])

return [int(first), int(second)]
```

## Run-time Analysis

The time complexity of this program is: `O(nlogn)`

The space complexity for this program is: `O(logn)`
