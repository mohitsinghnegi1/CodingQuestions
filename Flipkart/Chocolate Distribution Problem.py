# Qus:https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1


#User function Template for python3
import sys
class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        
        A.sort()
        min1 = sys.maxsize
        
        
        for i in range(N-M+1):
            min1 = min(min1,A[i+M-1]-A[i])
        return min1
        
        
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends