# Qus:https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        row = [0, 1, -1, 0]
        col = [-1, 0, 0, 1]

        def dfs(i, j):

            if (i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "2" or grid[i][j] == "0"):
                return

            grid[i][j] = "2"

            # 0+0,0+1 = 0,1

            for x in range(4):
                # print i+row[x],j+col[x],i,j
                dfs(i + row[x], j + col[x])

        count = 0
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == "1"):
                    dfs(i, j)
                    count += 1
        # print grid
        return count