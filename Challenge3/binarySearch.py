def binary_search(arr, key):
    first = 0
    last = len(arr) - 1
    if last % 2 != 0:
        last += 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            first = mid + 1
        else:
            last = mid - 1
    return -1


print(binary_search([4, 8, 15, 16, 23, 42], 15))
print(binary_search([4, 8, 15, 16, 23, 42], 42))

#nice!
