from Quick_Sort import quicksort


def rearrange_digits(input_list):
    size = len(input_list)
    if size <= 2:
        return input_list

    quicksort(input_list)

    first, second = '', ''
    for i in range(size - 1, -1, -2):
        first += str(input_list[i])
        if i - 1 >= 0:
            second += str(input_list[i - 1])

    return [int(first), int(second)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 2], [1, 2]])
test_function([[1, 2, 3], [1, 32]])
test_function([[], []])
