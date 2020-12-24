# Qus:https://leetcode.com/problems/maximum-length-of-repeated-subarray/
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        """
            Intution :
            
                Just use dp where a[i][j]=a[i-1][j-1]+1 if A[i]==B[j] 
            
        """

        out = []

        max1 = 0
        for i in range(len(A)):
            v = []
            for j in range(len(B)):
                if(A[i] == B[j]):
                    if(i != 0 and j != 0):
                        v.append(out[-1][j-1]+1)
                    else:
                        v.append(1)
                    max1 = max(max1, v[-1])
                else:
                    v.append(0)
            out.append(v)

        return max1
