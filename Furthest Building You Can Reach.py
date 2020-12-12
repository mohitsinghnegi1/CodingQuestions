# Qus:https://leetcode.com/problems/furthest-building-you-can-reach/

"""
Intution : Seen the Leetcode hits

using ladder  for greatest height first will gives us a optimal solution
and then bricks , once we reach to the situation where we dont have sufficient bricks 
then we will return index-1

"""


# this is my own solution time complexity len(height) *log K
from heapq import heappop, heappush


class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        maxIndex = 0
        prevHeight = heights[0]
        heapSum, totalSum = 0, 0

        heap = []

        for curHeight in heights:
            if(prevHeight < curHeight):
                if(len(heap) < ladders):
                    heapSum += (curHeight-prevHeight)
                    heappush(heap, curHeight-prevHeight)
                elif(len(heap) and heap[0] < (curHeight-prevHeight)):
                    top = heappop(heap)
                    heapSum += (curHeight-prevHeight-top)
                    heappush(heap, curHeight-prevHeight)

                totalSum += (curHeight-prevHeight)
                if(totalSum-heapSum > bricks):

                    return maxIndex-1

            prevHeight = curHeight
            # break if we dont want to increment the index
            maxIndex += 1
        return maxIndex-1


# easy to understand solution O(nlogK) time complexity


class Solution1(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """

        heap = []

        for i in range(1, len(heights)):

            curHeight = heights[i]

            diff = curHeight - heights[i-1]

            if(diff > 0):

                heappush(heap, diff)

                if(len(heap) > ladders):
                    bricks -= heappop(heap)

                    if(bricks < 0):
                        return i-1

        return len(heights)-1
