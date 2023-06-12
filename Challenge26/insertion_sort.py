def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr


print(insertion_sort([50, 10]))
print(insertion_sort([8, 4, 23, 42, 16, 15]))
print(insertion_sort([20, 18, 12, 8, 5, -2]))
print(insertion_sort([5, 12, 7, 5, 5, 7]))
print(insertion_sort([2, 3, 5, 7, 13, 11]))
