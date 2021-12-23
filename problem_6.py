import random


def get_min_max(arr):
    if len(arr) < 1:
        raise Exception("invalid input")

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
