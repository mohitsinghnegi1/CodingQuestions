# Qus:https://leetcode.com/problems/find-median-from-data-stream/
from heapq import heappush, heappop


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if(self.maxheap == []):
            heappush(self.maxheap, -num)
            return

        # balancing logic
        if(len(self.maxheap) <= len(self.minheap)):
            # put element in maxheap
            if(self.minheap[0] < num):
                num2 = heappop(self.minheap)
                heappush(self.minheap, num)
                heappush(self.maxheap, -num2)
            else:
                heappush(self.maxheap, -num)

        else:
            # put element in minheap
            if(-self.maxheap[0] > num):
                num2 = -heappop(self.maxheap)
                heappush(self.minheap, num2)
                heappush(self.maxheap, -num)
            else:
                heappush(self.minheap, num)

    def findMedian(self):
        """
        :rtype: float
        """
        if(len(self.maxheap) != len(self.minheap)):
            return -self.maxheap[0]

        return (-(self.maxheap[0]+0.0)+(self.minheap[0]+0.0))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# // light version


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        small, large = self.heaps

        heappush(large, -heappushpop(small, -num))

        if(len(small) <= len(large)):
            heappush(small, -heappushpop(large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps

        if(len(small) != len(large)):
            return -small[0]

        return (-small[0]+large[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
