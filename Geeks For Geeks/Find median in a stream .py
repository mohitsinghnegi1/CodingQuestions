# Qus:https://practice.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1
# TImeComplexity : O(nlogn)

# brute force solution would be using insertion sort
# little optimisation would be by using binary search
# optimised solution would be by using two heap (max , min)

# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import defaultdict
import math

# } Driver Code Ends
# User function Template for python3

''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''


class Solution:
    def __init__(self):
        self.lheap = []
        self.rheap = []
        self.count = 0

    def balanceHeaps(self):
        # Balance the two heaps size , such that difference is not more than one.
        # code here
        pass

    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''

    def getMedian(self):
        # return the median of the data received till now.
        # code here

        if(self.count == 0):
            return 0

        if(self.count % 2 == 0):
            # even number of eleement
            return (-self.lheap[0] + self.rheap[0])/2
        else:
            return -self.lheap[0]

    def insertHeaps(self, x):
        #:param x: value to be inserted
        #:return: None
        # code here

        # we have to maintain equal element in both heap
        if(self.count % 2 == 0):
            # insert in left
            if(self.rheap and self.rheap[0] < x):

                min1 = heapq.heappop(self.rheap)
                heapq.heappush(self.lheap, -min1)
                heapq.heappush(self.rheap, x)

            else:
                heapq.heappush(self.lheap, -x)
        else:
            if(-self.lheap[0] > x):
                max1 = heapq.heappop(self.lheap)
                heapq.heappush(self.rheap, -max1)
                heapq.heappush(self.lheap, -x)

            else:
                heapq.heappush(self.rheap, x)

        self.count += 1


# {
# Driver Code Starts.

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        ob = Solution()
        for i in range(n):
            x = int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends
