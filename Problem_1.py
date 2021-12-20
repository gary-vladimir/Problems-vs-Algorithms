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


def sqrt(number):
    return -1 if number < 0 else 1 if number == 1 else helper(number)


print("Pass" if (-1 == sqrt(-25)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
