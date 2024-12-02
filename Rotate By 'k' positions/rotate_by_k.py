# Implement a function to rotate an array by `k` positions.

def rotate_by_k(arr, num):
    print(arr[:num])
    print(arr[num:])
    print(arr[num:] + arr[:num])



k = 4
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
rotate_by_k(arr1, k)
