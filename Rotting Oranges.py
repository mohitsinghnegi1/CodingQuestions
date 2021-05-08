# Qus:https://leetcode.com/problems/rotting-oranges/
# Time complexity O(n*2) - to visit all the cells

from collections import deque

row = [0, 1, -1, 0]
col = [-1, 0, 0, 1]


def getNumberOfFreshOrg(grid):

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 1):
                count += 1

    return count


def isInside(n, m, ni, nj):

    if(ni < 0 or ni >= n or nj < 0 or nj >= m):
        return False
    return True


def getMinTimeToRotOrg(grid, nofreshOrg):

    n, m = len(grid), len(grid[0])
    timeInMin = 0

    queue = deque()

    # insert all the rotten oranges in queue and do dfs to find mintime to rot all oranges
    # if there left any fresh oranges then return -1
    # do bfs to do level order traversal and find minTime

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 2):
                queue.append((i, j, 0))

    # print queue
    # now we got all rotten oranges
    # now we need to find number of min

    # treverse until noOfFreshOrg is > 0 or queue is not empty
    while(queue and nofreshOrg):

        i, j, t = queue.popleft()

        for x in range(4):
            ni = i + row[x]
            nj = j + col[x]
            if(isInside(n, m, ni, nj) and grid[ni][nj] == 1):
                queue.append((ni, nj, t + 1))
                grid[ni][nj] = 2  # make this orange rotten
                timeInMin = t + 1
                nofreshOrg -= 1
                # print (ni,nj)

    return -1 if nofreshOrg else timeInMin


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if(len(grid) == 0):
            return 0

        nofreshOrg = getNumberOfFreshOrg(grid)  # correct
        # print nofreshOrg

        minTimeInMin = getMinTimeToRotOrg(grid, nofreshOrg)

        return minTimeInMin
