# QUs:https://leetcode.com/problems/unique-paths-ii/

# brute force
class Solution1(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if(len(grid) == 0 or len(grid[0]) == 0):
            return 0

        global count
        count = 0

        def setcount(i, j):
            global count
            if(i >= n or j >= m or j < 0 or i < 0 or grid[i][j] == 1):
                return
            if(i == n-1 and j == m-1):
                count += 1
                return

            # move right
            setcount(i, j+1)
            # move bottom
            setcount(i+1, j)

        n = len(grid)
        m = len(grid[0])

        i = j = 0
        setcount(i, j)

        return count


# solution using bottom up approach + dp (slow but submitted)

class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if(len(grid) == 0 or len(grid[0]) == 0):
            return 0

        d = {}

        def setcount(i, j):

            if(d.get((i, j), None)):
                return d[(i, j)]

            if(i >= n or j >= m or j < 0 or i < 0 or grid[i][j] == 1):
                return 0
            if(i == n-1 and j == m-1):

                return 1

            # move right
            r = setcount(i, j+1)
            # move bottom
            b = setcount(i+1, j)

            d[(i, j)] = r+b
            return r+b

        n = len(grid)
        m = len(grid[0])

        i = j = 0
        return setcount(i, j)

# optimized version using bottom up approach


class Solution2(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # doing bottom up approach
        # [[0,0],[0,1]] cornere test when the destination is already an obstacle
        if(len(grid) == 0 or len(grid[0]) == 0 or grid[-1][-1] == 1):
            return 0

        n = len(grid)
        m = len(grid[0])

        grid[n-1][m-1] = 1

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):

                if(grid[i][j] == 0):
                    # use grid[i][j]+  because for grid[-1][-1]
                    grid[i][j] += (grid[i][j+1] if j+1 < m else 0)
                    grid[i][j] += (grid[i+1][j] if i+1 < n else 0)
                elif not(i == n-1 and j == m-1) and grid[i][j] == 1:
                    grid[i][j] = 0
                    # skip it

        # print grid
        return grid[0][0]
