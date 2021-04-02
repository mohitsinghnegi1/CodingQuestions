# QUs:https://leetcode.com/problems/sliding-window-maximum/

# brute force solution
from collections import deque
import sys


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if(len(nums) == 0):
            return []
        # brute force
        out = []
        for i in range(len(nums)-k+1):
            max1 = -sys.maxsize
            for j in range(i, i+k):
                max1 = max(nums[j], max1)
            out.append(max1)
        return out

# efficient solution


class Solution2(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if(k <= 1):
            return nums

        dq = deque()

        # push the candidate out element's index inside queue

        for i in range(k):

            while dq:
                if(nums[dq[-1]] <= nums[i]):
                    dq.pop()
                else:
                    break
            dq.append(i)

        out = []
        print dq
        for i in range(k, len(nums)):
            out.append(nums[dq[0]])

            # check if left index in dequeu is still in range
            # if not pop left most index
            if(dq[0] < i-k+1):
                dq.popleft()

            while dq:
                # we need to compare value to pop out from the end of dq with the                     #current elemnt if current elemnt is greater then some of the                       #element in the dq then we will pop out those elemnet
                if(nums[dq[-1]] <= nums[i]):
                    dq.pop()
                else:
                    break
            dq.append(i)

        # also append the max elemnt in last window
        out.append(nums[dq[0]])

        return out


# TLE but solution using segment tree
# import math


class SegmentTree(object):

    # pass array from which we need to construct a segment tree
    def __init__(self, a):
        self.n = len(a)
        # height = int(ceil(log(self.n)))
        # size = 2*(int(pow(2,height)))-1
        size = 4*self.n
        self.st = [-1]*size

    def getTree(self):
        return self.st

    def build(self, nums, i, j, si=0):

        st = self.st
        # if range size is 1 (base case) we need to return max
        if(i == j):
            # print i
            st[si] = nums[i]
            return st[si]
        mid = (i+j)/2

        lmax = self.build(nums, i, mid, 2*si+1)
        rmax = self.build(nums, mid+1, j, 2*si+2)

        st[si] = max(lmax, rmax)
        return st[si]

    # remember we need to compare current range with the query range
    # current range if overlap then we need to return seg[si]
    def query(self, ql, qr, l, r, si):

        # if range complexte
        st = self.st

        if(l >= ql and r <= qr):  # completely lies inside
            # print l,r,ql,qr,si
            return st[si]

        # outside the range then return opposite value
        if(r < ql or l > qr):
            return -sys.maxsize

        mid = (l+r)/2
        lmax = self.query(ql, qr, l, mid, 2*si+1)
        rmax = self.query(ql, qr, mid+1, r, 2*si+2)

        # print l,r,max(lmax,rmax),"sd"
        return max(lmax, rmax)


class Solution3(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        s = SegmentTree(nums)
        s.build(nums, 0, n-1)
        # print s.getTree()
        out = []

        for i in range(n-k+1):
            # print i,i+k-1

            out.append(s.query(i, i+k-1, 0, n-1, 0))

        return out


# Revision : approch using sliding window and deque


class Solution4(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """
            Intution:
            use dequeue , push index , whenever you push some index pop from 
            last until the top elemtn is > the current 
            
            whenever we decrease the window size from left , we need to see if the front eleemtn
            in queue is same as current. index if so pop it 
            
            Note : we are just making sure that front element of dequeu is always max in a current window
            
            Time complexity O(N)
        
        
        
        """

        n = len(nums)
        out = []

        queue = deque([])

        def pushIntoDeque(i):
            while(len(queue) != 0 and nums[queue[-1]] <= nums[i]):
                queue.pop()
            queue.append(i)

        # find max in first k eleemnt and construct intial deque
        for i in range(k):
            pushIntoDeque(i)

        out.append(nums[queue[0]])

        for i in range(1, n-k+1):

            if(queue[0] == i-1):
                queue.popleft()

            pushIntoDeque(i+k-1)
            # print i,queue
            out.append(nums[queue[0]])
        return out
