# Qus:https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

def maxProfit(prices,i,buy):
        # print profit
        if(i>=len(prices)):
            return 0
        
        
        doBuy = 0
        doSell = 0
        
        if(buy):
            # we can choose to sell or not to sell
            doBuy = maxProfit(prices,i+1,True) # choose to keep the buy or choose not to sell
            doSell =prices[i]+maxProfit(prices,i+2,False)  # choose to sell, increase by 2 including cooldown
        else:
            # we can choose to buy or not to buy if last one is not buy
            doBuy = -prices[i]+maxProfit(prices,i+1,True) # choose to buy
            doBuy = max(doBuy,maxProfit(prices,i+1,False)) # choose not to buy
        # print doBuy,doSell
        return max(doBuy,doSell)
            
            
# optimised using memorization
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)==0):
            return 0
        
        return maxProfit(prices,0,False)


def maxProfit(prices,i,buy,d):
        # print profit
        if(i>=len(prices)):
            return 0
        if(d.get((i,buy),False)!=False):
            return d.get((i,buy))
        
        
        doBuy = 0
        doSell = 0
        
        if(buy):
            # we can choose to sell or not to sell
            doBuy = maxProfit(prices,i+1,True,d) # choose to keep the buy or choose not to sell
            doSell =prices[i]+maxProfit(prices,i+2,False,d)  # choose to sell, increase by 2 including cooldown
        else:
            # we can choose to buy or not to buy if last one is not buy
            doBuy = -prices[i]+maxProfit(prices,i+1,True,d) # choose to buy
            doBuy = max(doBuy,maxProfit(prices,i+1,False,d)) # choose not to buy
        # print doBuy,doSell
        
        d[(i,buy)] = max(doBuy,doSell)
        
        return d[(i,buy)]
            
            

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)==0):
            return 0
        d = {}
        return maxProfit(prices,0,False,d)

# after conversion into dp
def maxProfit(prices,i,buy,d):
        # print profit
        if(i>=len(prices)):
            return 0
        if(d.get((i,buy),False)!=False):
            return d.get((i,buy))
        
        
        doBuy = 0
        doSell = 0
        
        if(buy):
            # we can choose to sell or not to sell
            doBuy = maxProfit(prices,i+1,True,d) # choose to keep the buy or choose not to sell
            doSell =prices[i]+maxProfit(prices,i+2,False,d)  # choose to sell, increase by 2 including cooldown
        else:
            # we can choose to buy or not to buy if last one is not buy
            doBuy = -prices[i]+maxProfit(prices,i+1,True,d) # choose to buy
            doBuy = max(doBuy,maxProfit(prices,i+1,False,d)) # choose not to buy
        # print doBuy,doSell
        
        d[(i,buy)] = max(doBuy,doSell)
        
        return d[(i,buy)]
            
            
"""
    dp[i][buy] = represents ith day , buy represents whether i did purchsed last day or not profit
    ie buy = true means last day i buyed 
    
    
    recurrance relation:
    top to bottom
    
    dp[i][True] = max(dp[i+1][True],dp[i+2][False]+prices[i])   # chose sell or not to sell
    dp[i][False] = max(dp[i+1][False],dp[i+1][True]-prices[i]) # choose buy or not to buy
    
   
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if(n<2):
            return 0
        
        dp=[[0 for buy in range(2)] for i in range(n+2) ]
        # print dp
        for i in range(n-1,-1,-1):
            dp[i][True] = max(dp[i+1][True],dp[i+2][False]+prices[i])   # chose sell or not to sell
            dp[i][False] = max(dp[i+1][False],dp[i+1][True]-prices[i]) # choose buy or not to buy
            
            
        return dp[0][False]
    
    
    
    
    