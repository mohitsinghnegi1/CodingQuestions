# Qus: https: // leetcode.com/problems/range-sum-query-2d-immutable/
import sys


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        n = len(matrix)
        m = len(matrix[0])

        self.dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):

                self.dp[i][j] = matrix[i-1][j-1] + self.dp[i - 1][j] + \
                    self.dp[i][j - 1] - self.dp[i - 1][j - 1]

        # print self.dp

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum1 = self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - \
            self.dp[row1][col2+1] + self.dp[row1][col1]

        return sum1


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# using 2d prefix sum (O(n**4)) still tle


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        def getSum(row1, row2, col1, col2, dp):

            sum1 = dp[row2+1][col2+1] - dp[row2+1][col1]
            sum1 += (-dp[row1][col2+1] + dp[row1][col1])

            return sum1

        n = len(matrix)
        if(n == 0):
            return 0
        m = len(matrix[0])

        closest = -sys.maxsize

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):

                dp[i][j] = matrix[i-1][j-1] + dp[i - 1][j] + \
                    dp[i][j - 1] - dp[i - 1][j - 1]
        # print prefix

        for r1 in range(n):  # end row
            for c1 in range(m):  # end col

                for r2 in range(r1, n):
                    for c2 in range(c1, m):
                        sum1 = getSum(r1, r2, c1, c2, dp)
                        if(sum1 <= k and sum1 > closest):
                            closest = sum1
        return closest
