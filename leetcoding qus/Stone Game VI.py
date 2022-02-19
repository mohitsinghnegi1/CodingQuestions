# QUs:https://leetcode.com/problems/stone-game-vi/

class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        """
            Sort based on overall point or profit 
            all the index which contain the max overall profit will be taken first 
            to increase their max profit 
        
        """

        # sort based on the overall profit that one will get
        profit = [(aliceValues[i]+bobValues[i], i)
                  for i in range(len(aliceValues))]
        profit.sort(reverse=True)

        aliceScore = 0
        bobScore = 0

        for i in range(len(aliceValues)):
            # all the even place profit will be taken by alice to play optimally and same by bob
            if(i % 2 == 0):
                aliceScore += aliceValues[profit[i][1]]
            else:
                bobScore += bobValues[profit[i][1]]

        if(aliceScore > bobScore):
            return 1
        elif(aliceScore < bobScore):
            return -1
        return 0
