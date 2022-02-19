# Qus: https://leetcode.com/problems/out-of-boundary-paths/

# Timecomplexity: m*n*moves

def isOutside(m, n, cr, cc):

    if(0 <= cr < m and 0 <= cc < n):
        return False

    return True


row = [0, 1, -1, 0]
col = [-1, 0, 0, 1]


# use memo
def solve(m, n, maxMove, curRow, curColumn):

    if(isOutside(m, n, curRow, curColumn)):
        return 1

    if(maxMove == 0):
        return 0

    if(dp[curRow][curColumn][maxMove] != -1):
        return dp[curRow][curColumn][maxMove]

    # else move in all direction
    moves = 0
    for i in range(4):
        moves += solve(m, n, maxMove - 1, curRow + row[i], curColumn + col[i])

    dp[curRow][curColumn][maxMove] = moves
    return moves


class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        global dp
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        return solve(m, n, maxMove, startRow, startColumn) % (10**9+7)
