# Qus:https://www.interviewbit.com/problems/k-largest-elements/



from heapq import heappush, heappop
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # construct a min heap 
        # keep/retain the max size of k
        heap = []

        for val in A:

            if(len(heap)<B):
                heappush(heap,val)
            else:
                if(heap!=[] and heap[0]<val):
                    heappop(heap)
                    heappush(heap,val)
        

        return heap
                




