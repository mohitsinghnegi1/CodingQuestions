# Qus:https://leetcode.com/problems/find-k-closest-elements/


import sys
from collections import deque

# time compelxity = nlog(n)


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        arr.sort(key=lambda i: (abs(x - i), i))
        return sorted(arr[:k])

# time complexity = O(log(n))


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        def binarySearch(arr, x):

            l = 0
            r = len(arr)-1

            while(l < r):
                mid = (l+r)/2

                if(arr[mid] == x):
                    return mid
                elif(arr[mid] > x):
                    r = mid
                else:
                    l = mid + 1
            return l  # gives the place where we can insert number

        n = len(arr)

        ci = binarySearch(arr, x)

        ci = ci - \
            1 if (ci-1 >= 0 and abs(arr[ci-1]-x) <= abs(arr[ci]-x)) else ci
        ci = ci + 1 if (ci+1 < n and abs(arr[ci+1]-x) < abs(arr[ci]-x)) else ci

        print arr[ci]

        l = ci - 1
        r = ci + 1

        out = deque([arr[ci]])
        while(k-1):
            if(l >= 0 and r < len(arr)):
                if(abs(arr[l]-x) <= abs(arr[r]-x)):
                    out.appendleft(arr[l])
                    l -= 1
                else:
                    out.append(arr[r])
                    r += 1
            elif(l >= 0):
                out.appendleft(arr[l])
                l -= 1
            else:
                out.append(arr[r])
                r += 1
            k -= 1

        return out
