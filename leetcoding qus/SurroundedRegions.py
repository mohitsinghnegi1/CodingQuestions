# Qus:https://leetcode.com/problems/surrounded-regions/


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if(board == []):
            return board
        n = len(board)
        m = len(board[0])

        def dfs(i, j):
            if(i < 0 or i >= n or j < 0 or j >= m):
                return
            if(board[i][j] == 'X' or board[i][j] == 'S'):
                return
            board[i][j] = 'S'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        # apply dfs on border '0' pos
        # while dfs mark all 'O' as 'S'
        # avoid revist same element by use of 'S'
        for i in range(n):

            if(board[i][0] == 'O'):
                dfs(i, 0)
            if(board[i][m-1] == 'O'):
                dfs(i, m-1)

        for j in range(m):

            if(board[0][j] == 'O'):
                dfs(0, j)
            if(board[n-1][j] == 'O'):
                dfs(n-1, j)

        # once you applied dfs on all border 'O'
        # you need to mark all 'O' as 'X' and all 'S' as 'O'
        for i in range(n):
            for j in range(m):
                board[i][j] = 'XO'[board[i][j] == 'S']
        #print out
