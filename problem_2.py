def rotated_array_search(input_list, number):
    size = len(input_list)
    if size == 0 or (size == 1 and input_list[0] != number):
        return -1

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


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 1])
