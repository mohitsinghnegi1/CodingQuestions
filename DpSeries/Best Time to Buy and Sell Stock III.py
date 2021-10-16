# Qus:https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# recursive solution 2*n

def maxProfitUtil(prices,i,k,lastBuy):
    
    if(i>=len(prices) or k<=0):
        return 0
    
    buy = 0
    sell = 0
    
    if(lastBuy):
        sell = maxProfitUtil(prices,i+1,k-1,False) + prices[i]
        sell = max(sell,maxProfitUtil(prices,i+1,k,lastBuy)) # dont sell
        
    else:
        # i can buy or not buy
        buy = maxProfitUtil(prices,i+1,k,True) - prices[i]
        buy = max(buy,maxProfitUtil(prices,i+1,k,False)) # dont buy
    
    return max(buy,sell)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0 # this denotes the day number
        k = 2 # denotes the number of transactions 
        lastBuy = False # this will tell weather you already buy or not
        # you may not engage in multiple transactions
        return maxProfitUtil(prices,i,k,lastBuy)


# with memorization 
def maxProfitUtil(prices,i,k,lastBuy,d):
    
    if(i>=len(prices) or k<=0):
        return 0
    
    if(d.get((i,k,lastBuy),False)!=False):
        return d.get((i,k,lastBuy))
    
    buy = 0
    sell = 0
    
    if(lastBuy):
        sell = maxProfitUtil(prices,i+1,k-1,False,d) + prices[i]
        sell = max(sell,maxProfitUtil(prices,i+1,k,lastBuy,d)) # dont sell
        
    else:
        # i can buy or not buy
        buy = maxProfitUtil(prices,i+1,k,True,d) - prices[i]
        buy = max(buy,maxProfitUtil(prices,i+1,k,False,d)) # dont buy
    
    d[(i,k,lastBuy)] = max(buy,sell)
    
    return d[(i,k,lastBuy)]





class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0 # this denotes the day number
        k = 2 # denotes the number of transactions 
        lastBuy = False # this will tell weather you already buy or not
        # you may not engage in multiple transactions
        d= {}
        return maxProfitUtil(prices,i,k,lastBuy,d)