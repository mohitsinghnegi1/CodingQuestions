# Qus:https://www.geeksforgeeks.org/find-missing-element-in-a-sorted-array-of-consecutive-numbers/?ref=rp
# time complexity is O(nlogn)
def findMissing(arr, n):
    if(len(arr) == 0):
        return -1
    # if array is already valid
    if(arr[-1] == arr[0] + n - 1):
        return -1

    l = 0
    r = len(arr)
    while(l < r):
        mid = (l+r)/2

        # left side is valid
        if(arr[mid] == mid + arr[0]):
            if(arr[mid+1] > arr[mid]+1):
                return arr[mid]+1
            l = mid + 1

        else:
            if(arr[mid-1] < arr[mid]-1):
                return arr[mid]-1
            r = mid
    return


# Observation : arr[i] = index + arr[0]       arr[mid] == mid + arr[0]
arr = [1, 2, 4, 5, 6]
n = len(arr)

print(findMissing(arr, n))
