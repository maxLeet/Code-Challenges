# Explain and implement a quicksort or mergesort algorithm.
def merged_sort(arr, low, high):
    merged = [0] * len(arr)
    left , right = partition(arr)
    k = low
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        print("Comparison", left[i] ," - ", right[j])
        if left[i] <= right[j]:
            merged[k] = left[i]
            i+=1
        else:
            merged[k] = right[j]
            j+=1
        k+=1
    while i < len(left):
        merged[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        merged[k] = right[j]
        j+=1
        k+=1
    return merged
def partition(arr):
    midpoint = int(len(arr)/2)
    left = arr[:midpoint]
    right = arr[midpoint:]
    return left , right

if __name__ == '__main__':
    arr1 = [ 35, 45, 25, 11, 34, 22, 4, 7]
    print( merged_sort(arr1, 0 , len(arr1)-1) )
