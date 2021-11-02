# Qus:https://www.interviewbit.com/problems/first-non-repeating-character-in-a-stream-of-characters/

"""
    Keep track of frequency : print non repeating character based on this frequency
    use heap to find the min index non repeating char (optional)

"""

from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        d = {}
        s = ""
        heap = []

        for i in range(len(A)):
            val = A[i]
            

            if(val not in d):
                heappush(heap,(i,val))
                d[val] = 1
            else:
                d[val] += 1


            while(heap and d[heap[0][1]]!=1):
                i,val = heappop(heap)

            if(heap==[]):
                s+='#'
            else:
                s+=heap[0][1]
        return s



            

            

            



