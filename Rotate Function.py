# QUs:https://leetcode.com/problems/rotate-function/

import sys


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def F(k, A, last, prevans, sum1):

            # print BK

            k = len(A)*A[last]
            # print k,prevans,sum1
            ans = prevans+sum1-k
            return ans

        max1 = -sys.maxsize

        ans = sum([i*A[i] for i in range(len(A))])

        for i in range(1, len(A)+1):

            ans = F(i, A, len(A)-i, ans, sum(A))
            max1 = max(ans, max1)

        return max1 if max1 != -sys.maxsize else 0


# optimised way using formula f[i] = f[i-1]+sum1-n*A[n-i]
class Solution2(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)

        if(n <= 0):
            return 0

        sum1 = sum(A)

        F = [-1]*len(A)

        F[0] = sum([i*A[i] for i in range(len(A))])

        for i in range(1, len(A)):
            F[i] = F[i-1]+sum1-n*A[(n-i)]

        return max(F)

# you can futher optimise space using storing it in variable
