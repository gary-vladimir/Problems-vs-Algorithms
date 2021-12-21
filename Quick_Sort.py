def quicksort(array):
    sort(array, 0, len(array) - 1)


def sort(array, start_idx, end_idx):
    if start_idx >= end_idx:
        return

    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx

    while right_idx >= left_idx:
        pivot = array[pivot_idx]
        left = array[left_idx]
        right = array[right_idx]

        if left > pivot:
            swap(array, left_idx, right_idx)

        if left <= pivot:
            left_idx += 1
        if right >= pivot:
            right_idx -= 1

    swap(array, pivot_idx, right_idx)
    sort(array, start_idx, right_idx - 1)
    sort(array, pivot_idx + 1, end_idx)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
