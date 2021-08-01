# Qus:https://leetcode.com/problems/making-a-large-island/submissions/

# intution
"""
first find all the connected components assign a component numer to each componet which is greater then 1
for each zero see all the adj size and get the size of unique compoents attached to it
time complexity O(n**2)

"""

row = [0, 1, -1, 0]
col = [-1, 0, 0, 1]


def isInside(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m


def dfs(i, j, n, m, grid, no):

    stack = [(i, j)]
    grid[i][j] = no
    size = 0

    while(stack):
        i, j = stack.pop()
        size += 1
        for x in range(4):
            ni, nj = i+row[x], j+col[x]
            if(isInside(ni, nj, n, m) and grid[ni][nj] == 1):
                grid[ni][nj] = no
                stack.append((ni, nj))
    # print "dfs grid",grid,size
    return size


def getSize(i, j, n, m, grid, sizeMap):

    compNoSet = set()
    for x in range(4):
        ni, nj = i+row[x], j+col[x]
        if(isInside(ni, nj, n, m) and grid[ni][nj] != 0):
            compNoSet.add(grid[ni][nj])

    size = 1
    for i in compNoSet:
        size += sizeMap[i]

    return size


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        v = [[0]*m for _ in range(n)]

        sizeMap = {}  # componentNumber : size
        no = 2
        maxSize = 0

        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1):  # not visited
                    size = dfs(i, j, n, m, grid, no)
                    sizeMap[no] = size
                    maxSize = max(maxSize, size)
                    no += 1
                    # print "=> ",i,j,grid
        # print sizeMap
        maxSizeIsland = 0

        # do other stuff
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 0):
                    size = getSize(i, j, n, m, grid, sizeMap)
                    maxSizeIsland = max(maxSizeIsland, size)

        return maxSize if maxSizeIsland == 0 else maxSizeIsland
