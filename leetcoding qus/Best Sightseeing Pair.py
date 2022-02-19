# Qus:https://leetcode.com/problems/best-sightseeing-pair/

# always see what we need to maximize or minimize in this type of question

class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        dp = [0]*len(values)
        
        dp = values[0]
        
        ans = 0
        
        for i in range(1,len(values)):
            
            
            ans = max(ans,dp+values[i]-i)
            dp = max(dp,values[i]+i)
        # print dp
        return ans
            