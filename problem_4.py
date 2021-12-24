import numpy


def sort_012(input_list):
    if len(input_list) <= 0:
        return input_list

    unique, counts = numpy.unique(numpy.array(input_list), return_counts=True)
    zeros = counts[0]
    ones = counts[1]
    twos = counts[2]

    return ([0] * zeros) + ([1] * ones) + ([2] * twos)


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
