# Qus:https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1
# User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here

        # dp[i] # i weight allowed , dp[i] will tell what is the max profit
        dp = [0]*(W+1)

        for w in range(1, W+1):

            for j in range(N):
                dp[w] = max(dp[w - wt[j]]+val[j]
                            if(w - wt[j] >= 0) else 0, dp[w])
        return dp[W]


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])

        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends
