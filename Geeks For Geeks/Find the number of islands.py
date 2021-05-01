# 9 3
# 0 1 0
# 0 1 0
# 0 0 0
# 1 1 0
# 1 0 1
# 0 1 1
# 1 1 1
# 0 1 1
# 1 0 1


row = [1, 0, -1, 1, -1, 1, 0, -1]
col = [-1, -1, -1, 0, 0, 1, 1, 1]


def findIsands(grid, n, m, i, j, visited):
    if(i < 0 or j < 0 or i >= n or j >= m or visited[i][j] == 1 or grid[i][j] == '0'):
        return
    visited[i][j] = 1
    # traverse in all eight directions
    for x in range(8):
        findIsands(grid, n, m, i+row[x], j+col[x], visited)


class Solution:
    def numIslands(self, grid):
        # Code here

        n, m = len(grid), len(grid[0])

        visited = [[-1 for _ in range(m)] for _ in range(n)]
        noOfIslands = 0

        for i in range(n):
            for j in range(m):
                if(visited[i][j] == -1 and grid[i][j] == '1'):
                    findIsands(grid, n, m, i, j, visited)
                    noOfIslands += 1

        return noOfIslands


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = map(int, raw_input().split())
        grid = []
        for _ in range(n):
            a = list(raw_input().split())
            grid.append(a)
        obj = Solution()
        ans = obj.numIslands(grid)
        print(ans)

# } Driver Code Ends
