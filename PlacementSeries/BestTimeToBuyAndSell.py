# Qus:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices) == 0):
            return 0

        maxProfit = 0
        min1 = prices[0]

        for i in range(1, len(prices)):
            min1 = min(prices[i], min1)
            maxProfit = max(maxProfit, prices[i]-min1)
        return maxProfit
