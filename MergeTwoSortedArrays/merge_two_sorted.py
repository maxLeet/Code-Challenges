# Write a function to merge two sorted arrays into a single sorted array.
from collections import deque
def merged_two_sorted(arr1, arr2):
    merged = []
    a = deque(arr1)
    b = deque(arr2)
    print("Total number of elements", len(a) + len(b) )
    while len(a) + len(b) > 0:
        if len(a) > 0:
            if len(b) > 0:
                if a[0] < b[0]:
                    print(a[0]," < ", b[0])
                    merged.append(a.popleft())
                else:
                    print(a[0]," > ", b[0])
                    merged.append(b.popleft())
            else:
                print("B is empty")
                merged.append(a.popleft())
        else:
            print("A is empty")
            merged.append(b.popleft())
    print("Total merged elements", len(merged))
    return merged


if __name__ == '__main__':
    one = [1, 23, 25, 35, 47, 50]
    two = [2, 3, 4, 5, 24, 27, 36, 48]
    print( merged_two_sorted(one, two) )
    print
