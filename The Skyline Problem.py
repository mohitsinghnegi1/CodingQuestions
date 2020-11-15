# QUs:https://leetcode.com/problems/the-skyline-problem/
from heapq import *


def getArray(buildings):

    arr = []

    for s, e, h in buildings:

        # 0 represents start
        # 1 represents end
        arr.append((s, h, 0))
        arr.append((e, h, 1))

    return arr


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # get the array in the form s and e points of a buildings
        # For example [(xs,h,0),(xe,h,1)]
        arr = getArray(buildings)

        # sort it based on (x then in case of tie if it is start then it should come first
        # if it is end then smaller building should come first
        '''
             _______          ________
            |___    |        |    ____|
            |   |   |   or   |    |   |
        '''

        sarr = sorted(arr, key=lambda x: (x[0], x[1] if x[2] else -x[1]))

        out = []
        heap = [0]
        # we are using min heap so to. make it max eap we need to push -val

        for x, h, se in sarr:

            # if start of building
            if(se == 0):
                top = -heap[0]
                # if top is less then cur then add to to out
                if(top < h):
                    out.append([x, h])
                # push it to heap
                heappush(heap, -h)

            else:
                # if end of building

                beforeHeight = heap[0]
                # remove only one occurance
                heap.remove(-h)
                # since we have removed one element we need to heapify
                heapify(heap)
                afterHeight = heap[0]

                if(beforeHeight != afterHeight):
                    # means height changes
                    # we need to add to out with new height
                    out.append((x, -afterHeight))

        return out


# Optimization of heap deletion using dict********* New Learning
# If you do need to take an item out of the heap but want to preserve the heap you could do it lazily
# and discard it when the item comes out naturally, rather than searching through the list for it.
# If you store items you want to remove in a blacklist set, then each time you heapq.heappop check
# if that item is in the set. If it exists discard it and heappop again until you get something
# that's not blacklisted, or the heap is empty

# optimal O(nlog n) solution using Lazy deletion
# QUs:https://leetcode.com/problems/the-skyline-problem/


def getArray(buildings):

    arr = []

    for s, e, h in buildings:

        # 0 represents start
        # 1 represents end
        arr.append((s, h, 0))
        arr.append((e, h, 1))

    return arr


class Solution:
    def getSkyline(self, buildings):
        # get the array in the form s and e points of a buildings
        # For example [(xs,h,0),(xe,h,1)]
        arr = getArray(buildings)

        # sort it based on (x then in case of tie if it is start then it should come first
        # if it is end then smaller building should come first
        '''
             _______          ________
            |___    |        |    ____|
            |   |   |   or   |    |   |
        '''

        sarr = sorted(arr, key=lambda x: (x[0], x[1] if x[2] else -x[1]))

        out = []
        heap = [0]
        # we are using min heap so to. make it max eap we need to push -val
        deleteSet = {}

        def deleteEl(heap):
            # delete element that is already in delete set
            while(deleteSet.get(-heap[0], 0) > 0):
                deleteSet[-heap[0]] -= 1
                heappop(heap)

        for x, h, se in sarr:
            deleteEl(heap)
            # if start of building
            if(se == 0):

                # before seeing the top we need to remove delete set elements if any

                top = -heap[0]
                # if top is less then cur then add to to out
                if(top < h):
                    out.append([x, h])
                # push it to heap
                heappush(heap, -h)

            else:
                # if end of building we need to pop out the elements that is in delete set

                # only if the talest building is of same height the only effect will take                 # place

                if(heap[0] == -h):
                    beforeHeight = heap[0]
                    heappop(heap)
                    # may be possible that the next elemtn is in delete set
                    deleteEl(heap)
                    # now we are sure that top elemnt is not the element that is in delete                     # set
                    afterHeight = heap[0]

                else:
                    # height is not same then we need to add this to delete list
                    deleteSet[h] = deleteSet.get(h, 0)+1

                    beforeHeight = afterHeight = heap[0]

                if(beforeHeight != afterHeight):
                    # means height changes
                    # we need to add to out with new height
                    out.append((x, -afterHeight))

        return out
