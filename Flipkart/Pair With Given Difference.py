# Qus:https://www.interviewbit.com/problems/pair-with-given-difference/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):


        d = {}

        for i in range(len(A)):
            val = A[i]

            if(val + B in d or val - B in d):
                return 1
            d[val] = True
        return 0
