# QUs:https://leetcode.com/problems/coin-change/

#brute force approach
class Solution(object):
    def __init__(self):
        self.mincoin=-1
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.mincoin=sys.maxsize
        def solve(coins,i,target,count):
            
            if(target==0):
                self.mincoin=min(count,self.mincoin)
            
            if(i>=len(coins)):
                return
            
        
            if(target-coins[i]==0):
                self.mincoin=min(count+1,self.mincoin)
                return 
            if(target-coins[i]>0):
                solve(coins,i,target-coins[i],count+1)
                solve(coins,i+1,target,count)
            else:
                solve(coins,i+1,target,count)
        
        
        
        coins.sort(reverse=True)
        
        solve(coins,0,amount,0)
        return self.mincoin if self.mincoin!=sys.maxsize else -1

#remember dont think that 5 5 1 1 1 1  will not give optimal result 
# 5 5 4 is more optimal to choose

#efficient solution
class Solution(object):
    def __init__(self):
        self.mincoin=sys.maxsize
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if(amount==0):
            return 0
        if(len(coins)==0):
            return -1
        
        #each element at index i of this array represent 
        #what is the min number of coins required to get a value i
        minCoins=[sys.maxsize]*(amount+1)
        #to get a value 0 we need min 0 number of coins 
        minCoins[0]=0
        coins.sort()
        
        for i in range(1,amount+1):
            #try out each coin and substract from current i and update min coin at current position
            for j in range(len(coins)):
                if(i-coins[j]<0):
                    break
                if(minCoins[i-coins[j]]+1<minCoins[i]):
                    minCoins[i]=minCoins[i-coins[j]]+1
                
        #incase current position is sys.maxsize then it means not posssible to make that sum
        return minCoins[-1] if minCoins[-1]!=sys.maxsize else -1
        
        
        
     