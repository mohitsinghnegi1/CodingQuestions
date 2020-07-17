from collections import defaultdict
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        p1=defaultdict(int)
        for i in range(len(A)):
            for j in range(len(B)):
                p1[A[i]+B[j]]+=1
        
        out=0
        p2=defaultdict(int)
        for i in range(len(C)):
            for j in range(len(D)):
                out+=p1.get(-C[i]-D[j],0)
        return out
        
        
                
        
                