# Qus:https://www.interviewbit.com/problems/distribute-candy/
# time complexity : 2*O(N)

class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):

        if(len(A)==0):
            return 0

        dp = [1]
        c = 1

        for i in range(1,len(A)):
            if(A[i-1]<A[i]):
                c += 1
            else:
                c=1
            dp.append(c)

        c = 1
        

        for i in range(len(A)-2,-1,-1):

            if(A[i]>A[i+1]):
                c+=1
            else:
                c=1
            dp[i] = max(c,dp[i])

        return sum(dp)








