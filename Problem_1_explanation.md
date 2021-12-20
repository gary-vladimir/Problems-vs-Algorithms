# Square Root of an Integer

> Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

## Solution Explanation

The firs thing I did, was to check if the passed number was smaller than 0, if that is the case, it returns -1 always, because any negative number is invalid.

If that condition wasn't True, then check if the passed number is equal to 1, if that condition it's True, return 1. Else, meaning that the passed number is bigger than 1 use the helper function that takes the number

```python
def sqrt(number):
    return -1 if number < 0 else 1 if number == 1 else helper(number)
```

I decided to approach this problem with a Binary search algorithm to find the square root of the number

```python
def helper(number):
    low = 0
    high = number

    while low <= high:
        mid = (low + high) // 2
        if (mid**2 == number) or (mid**2 <= number and (mid+1)**2 > number):
            return mid
        elif (mid**2 > number):
            high = mid
        else:
            low = mid
```

## Run-time Analysis

The time complexity of this program is: `O(logn)`

The space complexity for this program is: `O(logn)`
