def binarySearch(arr, left, r, x):
    while r >= left:

        mid = (left + r) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid-1
        else:
            left = mid+1
    return None

def solution():
    n = int(input())
    parts = list(map(int, input().split()))
    m = int(input())
    requests = list(map(int, input().split()))

    parts.sort()

    for i in range(m):
        result = binarySearch(parts, 0, len(parts)-1, requests[i])
        if result != None:
            print("yes", end=" ")
        else:
            print("no", end=" ")

