# Qus:https://leetcode.com/problems/01-matrix/
from collections import deque


def isInside(newi, newj, n, m):

    return newi >= 0 and newj >= 0 and newi < n and newj < m
# time complity O(n*2)


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = [0, 1, -1, 0]
        cols = [-1, 0, 0, 1]

        n = len(mat)
        m = len(mat[0])
        queue = deque([])

        visited = [[False for col in range(m)] for row in range(n)]

        for i in range(n):
            for j in range(m):
                if(mat[i][j] == 0):
                    queue.append((i, j))
                    visited[i][j] = True
        # print visited
        while(queue):

            i, j = queue.popleft()
            # print i,j,(i==0 and j==4),mat[i][j]+1
            for z in range(4):
                newi, newj = i+rows[z], j+cols[z]
                if isInside(newi, newj, n, m) and not visited[newi][newj]:
                    mat[newi][newj] = mat[i][j]+1
                    visited[newi][newj] = True
                    queue.append((newi, newj))
        return mat


# to optimise space try out dp solution
