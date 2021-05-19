# QUs: https: // www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/
# resource: https: // www.youtube.com/watch?v = hVl2b3bLzBw & list = PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2 & index = 4


import math


def nextGap(gap):
    if(gap == 1):
        return 0

    return gap//2+1 if gap % 2 else gap//2


t = int(input())
for i in range(t):

    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    gap = n+m
    gap = nextGap(gap)

    while(gap):
        i = 0
        # first array
        while(i+gap < n):

            if(a[i] > a[i+gap]):
                a[i], a[i+gap] = a[i+gap], a[i]
            i += 1

        # both array

        while(i < n and i+gap < n+m):
            if(a[i] > b[i+gap-n]):
                a[i], b[i+gap-n] = b[i+gap-n], a[i]
            i += 1

        # second array
        while(i+gap < n+m):
            if(b[i-n] > b[i+gap-n]):
                b[i-n], b[i+gap-n] = b[i+gap-n], b[i-n]

            i += 1

        gap = nextGap(gap)

    # print both array
    for i in a:
        print(i, end=' ')

    for i in b:
        print(i, end=' ')

    print()


# next revision
# User function Template for python3
# time complexity O(n)*nlog(n+m)

class Solution:

    # Function to merge the arrays.
    def merge(self, arr1, arr2, n, m):
        # code here

        n = len(arr1)
        m = len(arr2)
        gap = (n+m)//2 + (n+m) % 2 if (n+m) > 1 else 0
        while(gap):
            i = 0
            while(i+gap < n+m):
                a = b = None
                if(i+gap < n):
                    # means both lie in same side
                    if(arr1[i] > arr1[i+gap]):
                        arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]

                # if both lie in different side
                if(i < n and i+gap >= n):
                    if(arr1[i] > arr2[i+gap-n]):
                        arr1[i], arr2[i+gap-n] = arr2[i+gap-n], arr1[i]
                if(i >= n):
                    if(arr2[i-n] > arr2[i+gap-n]):
                        arr2[i-n], arr2[i+gap-n] = arr2[i+gap-n], arr2[i-n]
                i += 1
            gap = gap//2+(gap % 2) if gap > 1 else 0  # ceil
            # print(gap)


# {
#  Driver Code Starts
# Initial template for Python
if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n, m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1, end=" ")
        print(*arr2)
# } Driver Code Ends
