# QUs:https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

import sys


class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)

        global minDifficultySoFar
        minDifficultySoFar = sys.maxsize

        def solve(i, n, daysLeft, sum1):

            # print i,n,daysLeft,sum1
            global minDifficultySoFar

            if(daysLeft < 0):
                return
            if(n == i and daysLeft == 0):
                minDifficultySoFar = min(
                    minDifficultySoFar, sum1+sum(jobDifficulty[i:]))
                return

            max1 = - sys.maxsize

            for j in range(i, n):
                # print j,n,daysLeft,n-daysLeft
                max1 = max(jobDifficulty[j], max1)
                solve(j+1, n, daysLeft-1, sum1+max1)

        # i : use keep track of i.. j max element
        # n : number of element left
        # d : number of days left
        # sum1 : sum of job in each days

        solve(0, n, d, 0)
        return minDifficultySoFar if minDifficultySoFar != sys.maxsize else -1


# efficient approach
"""
    Divide the array in d parts such that we need to return min sum of  subpartition such that the sum of max element of each part is min 
    of all sub partition

"""


class Solution2(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)

        suffixMax = [0]*n
        suffixMax[-1] = jobDifficulty[-1]

        for i in range(n-2, -1, -1):
            suffixMax[i] = max(jobDifficulty[i], suffixMax[i+1])

        # dp[i][j]  = for i days remaining  , and j element remaining what is the ans
        dp = [[-1]*(n+1) for i in range(d+1)]

        def solve(i, daysLeft):

            if(dp[daysLeft][i] != -1):
                return dp[daysLeft][i]
            # in case there is no enough element left for each partition
            # in that case return -1
            if(n < daysLeft):
                dp[daysLeft][i] = -1
                return dp[daysLeft][i]
            # in case dysLeft  is 1 then we have to take max from all the remaining array
            # this remaining array will be the last partition and we need to return max from it
            if(daysLeft == 1):
                dp[daysLeft][i] = suffixMax[i]
                return dp[daysLeft][i]
            ans = sys.maxsize
            max1 = -sys.maxsize
            for j in range(i, n-daysLeft+1):
                # max1 is the max in subarray
                max1 = max(max1, jobDifficulty[j])
                # cut at j : number of days left is reduced by 1
                # global ans is the min sum of  maxelement of all subarrays
                subSolution = solve(j+1, daysLeft-1)
                # # if ans received is -1 which is not possible as we are using n-daysLeft+1
                # there will be always devision avaible
                # if(subSolution!=-1):
                ans = min(ans, max1+subSolution)

            dp[daysLeft][i] = ans
            return dp[daysLeft][i]

        return solve(0, d)
