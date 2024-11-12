def binary_search_rec(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_rec(arr, target, low, mid -1)
    else:
        return binary_search_rec(arr, target, mid+1, high)

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search_rec(arr, 17, 0, len(arr) - 1))