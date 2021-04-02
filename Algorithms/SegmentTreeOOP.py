# Qus: https: // leetcode.com/problems/sliding-window-maximum/
import sys
import math


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


class Solution(object):
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
