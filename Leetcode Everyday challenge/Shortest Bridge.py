#  O(N**2) using dfs, bfs
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        queue = []

        def dfs(i,j):
            # make sure not to visit the same marked island again
            if(i<0 or i>=n or j<0 or j>=m or grid[i][j]==0 or grid[i][j]==2):
                return

            if(grid[i][j]==1):
                queue.append((i,j,0))
                grid[i][j]=2

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)



        flag = True

        for i in range(n):
            for j in range(m):

                if(grid[i][j]==1):
                    # mark as 2 and append in stack
                    dfs(i,j)
                    flag = False
                    break

            if(flag==False):
                break

        # print queue

        row = [0,1,-1,0]
        col = [-1,0,0,1]

        # use bfs to find min dist

        def inside(newR,newC,n,m):


            return newR>=0 and newR<n and newC>=0 and newC<m;



        while(queue):

            i,j,l = queue.pop(0)
            # print i,j,l
            for x in range(4):

                newR = i+row[x]
                newC = j+col[x]
                if(inside(newR,newC,n,m)):


                    if(grid[newR][newC]==0):
                        queue.append((newR,newC,l+1))
                        grid[newR][newC]=2

                    elif(grid[newR][newC]==1):
                        return l






































