# Qus:https://leetcode.com/problems/pacific-atlantic-water-flow/

# time complexity n*m*(E + V) ~ O(n**3)

from collections import deque


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        """
            Intution :
            traverse in each cell and for each cell do dfs  
            if the water can flow in both oceans then we will add this coordinate to the coordinate list  
            I used visited list to prevent revisit of alrready visited cell
        
        
        """

        n = len(matrix)
        if(n == 0):
            return []
        m = len(matrix[0])
        if(m == 0):
            return []

        def dfs(i, j, n, m):
            leftTop = False
            bottomRight = False

            stack = [(i, j)]

            v = {}
            v[(i, j)] = True
            while(stack):

                x, y = stack.pop()

                if(x-1 < 0):
                    leftTop = True
                elif(matrix[x-1][y] <= matrix[x][y]):

                    if((x-1, y) not in v):
                        stack.append((x-1, y))
                        v[(x-1, y)] = True

                if(y-1 < 0):
                    leftTop = True

                elif(matrix[x][y-1] <= matrix[x][y]):

                    if((x, y-1) not in v):

                        stack.append((x, y-1))
                        v[(x, y-1)] = True

                if(x+1 >= n):
                    bottomRight = True
                elif(matrix[x+1][y] <= matrix[x][y]):
                    if((x+1, y) not in v):

                        stack.append((x+1, y))
                        v[(x+1, y)] = True

                if(y+1 >= m):
                    bottomRight = True

                elif(matrix[x][y+1] <= matrix[x][y]):
                    if((x, y+1) not in v):

                        stack.append((x, y+1))
                        v[(x, y+1)] = True

                if(leftTop and bottomRight):
                    return True

            return leftTop and bottomRight

        coordinates = []
        for i in range(n):
            for j in range(m):
                if(dfs(i, j, n, m)):
                    coordinates.append([i, j])
        return coordinates


# need to optimise above approach O(n*2)


class Solution2(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        """
            Intution:
            
            find the cell who can reach the ocean : lets oppose the condition
            now find all the cell whose value is >= current cell value from which water can flow to ocean
            
            do this for both oceans 
            
            Note : here we need to maintain the cell list which is visited during traversal , which is the cells through which water can flow to ocean
            
            at the end we need to find the common cells through which water can flow in both oceans
        
        
        """

        if not matrix or not matrix[0]:
            return []

        n = len(matrix)
        m = len(matrix[0])

        pacific = deque()
        vp = set()

        atlantic = deque()
        va = set()

        for i in range(n):
            pacific.append((i, 0))
            vp.add((i, 0))
            atlantic.append((i, m-1))
            va.add((i, m-1))

        for j in range(m):
            pacific.append((0, j))
            vp.add((0, j))
            atlantic.append((n-1, j))
            va.add((n-1, j))

        row = [-1, 1, 0, 0]
        col = [0, 0, -1, 1]

        def dfs(queue, v):

            while(queue):
                i, j = queue.popleft()

                for k in range(4):

                    if(i + row[k] >= 0 and i + row[k] < n and j + col[k] >= 0 and j+col[k] < m):

                        cdnt = (i+row[k], j+col[k])
                        if cdnt not in v and matrix[cdnt[0]][cdnt[1]] >= matrix[i][j]:
                            v.add(cdnt)
                            queue.append(cdnt)

            return v

        dfs(pacific, vp)
        # print vp
        dfs(atlantic, va)
        # print va

        return list(vp.intersection(va))
