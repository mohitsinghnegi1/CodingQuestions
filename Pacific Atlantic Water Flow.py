# Qus:https://leetcode.com/problems/pacific-atlantic-water-flow/

# time complexity n*m*(E + V) ~ O(n**3)

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


# need to optimise above approach
