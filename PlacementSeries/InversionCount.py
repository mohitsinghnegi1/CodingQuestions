# Qus:https://www.geeksforgeeks.org/counting-inversions/

# practice: https: // practice.geeksforgeeks.org/problems/inversion-of-array/0

# --brute force using intsertion sort

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    icount = 0
    for i in range(n-1):
        for j in range(n-1):
            if(a[j] > a[j+1]):
                icount += 1
                a[j+1], a[j] = a[j], a[j+1]
    print(icount)


# ---optimal solution using merge sort

t = int(input())


def merge(a, l, mid, r):

    out = []
    i = l
    j = mid
    icount = 0

    while(i < mid and j <= r):
        if(a[i] > a[j]):
            # icount = mid-i because all element in right are also greater
            # then a[j]
            icount += mid-i
            out.append(a[j])
            j += 1
        else:
            out.append(a[i])
            i += 1

    # add remaining elemnt of the left arry
    while(i < mid):
        out.append(a[i])
        i += 1

    # add remaining elemnt to the right array
    while(j <= r):
        out.append(a[j])
        j += 1

    # copy all the element in orignal array
    for i in out:
        a[l] = i
        l += 1

    return icount


def mergeSort(a, l, r):
    if(l < r):
        mid = (l+r)//2
        icount = 0
        # divide full array into two equal parts
        icount += mergeSort(a, l, mid)
        icount += mergeSort(a, mid+1, r)
        # merge two sorted arrays
        icount += merge(a, l, mid+1, r)
        return icount
    return 0


for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # merge sort will return total inversion count in a
    icount = mergeSort(a, 0, n-1)

    print(icount)
