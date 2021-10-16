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


# using prefixProfit and suffixProfit array
# time complexity O(n**2)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        
        # 0..i,   i+1...n-1
        
        prefixPft = [0]*n
        suffixPft = [0]*n
        
        min1 = prices[0]
        
        for i in range(1,n):
            prefixPft[i] = max(prefixPft[i-1],prices[i]-min1)
            min1 = min(min1,prices[i])
            
        max1 =  prices[-1]  
        for i in range(n-2,-1,-1):
            suffixPft[i] = max(suffixPft[i+1],max1 - prices[i])
            max1 = max(max1,prices[i])
        
        maxProfit = 0
        
        
        for i in range(n+1):
            
            p1 = suffixPft[i] if i<n else 0
            p2 = prefixPft[i-1] if i-1>=0 else 0
            
            maxProfit = max(maxProfit,p1+p2)
        
        
        return maxProfit
        
        
        