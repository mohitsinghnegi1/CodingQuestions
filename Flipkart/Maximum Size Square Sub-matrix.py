# Qus:https://www.interviewbit.com/problems/maximum-size-square-sub-matrix/
# time complexity O(N**2)
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        max1 = 0

        for i in range(len(A)):
            for j in range(len(A[0])):

                if(A[i][j]==1):
                    max1 = max(max1,1)

                    if(i-1>=0 and j-1>=0):
                        A[i][j] = 1 + min(A[i-1][j-1],A[i-1][j],A[i][j-1])
                        max1 = max(max1,A[i][j])
        return max1**2
                        

