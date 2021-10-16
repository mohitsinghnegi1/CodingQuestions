# Qus:https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# recursion + memorization

def  maxProfitUtil(self, prices, fee,i,lastBuy,d):
    
    if(i>=len(prices)):
        return 0
    if(d.get((i,lastBuy),False)!=False):
        return d.get((i,lastBuy))
    
    sell = 0
    buy = 0
    
    if(lastBuy):
        # either sell or dont sell
        sell = maxProfitUtil(self, prices, fee,i+1,False,d) + prices[i] - fee
        sell = max(sell,maxProfitUtil(self, prices, fee,i+1,True,d))
    else:
        # either buy or dont buy
        buy = maxProfitUtil(self, prices, fee,i+1,True,d) - prices[i]
        buy = max(buy,maxProfitUtil(self, prices, fee,i+1,False,d))
    d[(i,lastBuy)] = max(sell,buy)
    return d[(i,lastBuy)]
    
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        #noof transaction min
        #profit max
        i = 0
        lastBuy = False
        d = {}
        
        return maxProfitUtil(self, prices, fee,i,lastBuy,d)

# using top down dp
 

"""
    Recurrance relation:
        dp[i][lastBuy] = represents i day what is the profit if i have last Buy as true or false
        dp[i][True] = max(dp[i+1][False]+prices[i]-fee, dp[i+1][True])
        dp[i][False] = max(dp[i+1][True]-prices[i],dp[i+1][False])



"""



class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        #noof transaction min
        #profit max
        n = len(prices)
    
        dp = [[0 for lastBuy in range(2)] for i in range(n+1)]
        
        for i in range(n-1,-1,-1):
            dp[i][True] = max(dp[i+1][False]+prices[i]-fee, dp[i+1][True])
            dp[i][False] = max(dp[i+1][True]-prices[i],dp[i+1][False])
        
        return dp[0][False]
        
        
        
    
    
     