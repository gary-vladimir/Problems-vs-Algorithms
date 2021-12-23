import random


def get_min_max(arr):
    if len(arr) < 1:
        return arr

    min_num = arr[0]
    max_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return min_num, max_num


l = [i for i in range(0, 10)]
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(35, 2001)]
random.shuffle(l)

print("Pass" if ((35, 2000) == get_min_max(l)) else "Fail")
print("Pass" if ([] == get_min_max([])) else "Fail")
