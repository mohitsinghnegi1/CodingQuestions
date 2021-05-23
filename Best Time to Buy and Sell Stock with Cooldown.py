# QUs:https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # dp[i][j]

        """
        dp[0][0] = you can't sell on day 0 so 0
        dp[0][1] = you buy : = - prices[i]  you are on loss currently
        dp[0][2] = you can't be on cooldown on day 0 so = 0
        
        
        """
        n = len(prices)

        if(n < 2):
            return 0

        dp = [[0]*2 for i in range(n)]

        dp[0][1] = -prices[0]
        dp[0][0] = 0

        dp[1][1] = max(-prices[1], dp[0][1])
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])

        for i in range(2, n):

            # when could i buy?
            # cooldown 1 step before
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            # or i have already buyed
            # before i have already purchased and i am selling it or i am on hold (on cooldown) so last selling price is same
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])

        # print dp
        return dp[n-1][0] if dp[n-1][0] > 0 else 0
