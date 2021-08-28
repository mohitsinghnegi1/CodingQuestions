# Qus:https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3950/
# time complexity O(N**2)

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # dp[i] = max profit uptil ith time
        n = len(startTime)
        sep = [[-1,-1,-1]]+zip(startTime, endTime, profit) #start end profit
        
        sep.sort(key=lambda x:(x[1]))
        # print sep
        
        dp = [0]*(sep[-1][1]+1)
        # print dp
        
        i = 1
        for s,e,p in sep:
            
            while(i<=e ):
                
                dp[i] = max(dp[i-1],dp[i])
                i+=1
            
            dp[e] = max(dp[e],dp[s] + p)
            
        # print dp
        return dp[-1]