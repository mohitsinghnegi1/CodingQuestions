# QUs:https://leetcode.com/problems/n-queens/
# https://www.youtube.com/watch?v=i05Ju7AftcM

import sys
sys.setrecursionlimit(1500)


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        chess = ["."*n for _ in range(n)]

        ans = []

        def isSafe(row, col):
            # print row,col
            n = len(chess)
            # see top
            # left digonal
            # right diagonal if there is already any queen
            # in these case return False
            i, j = row-1, col
            while(i >= 0):
                if(chess[i][j] == 'Q'):
                    return False
                i -= 1
            i, j = row-1, col-1
            while(i >= 0 and j >= 0):
                if(chess[i][j] == 'Q'):
                    return False
                i -= 1
                j -= 1

            i, j = row-1, col+1
            while(i >= 0 and j < n):
                if(chess[i][j] == 'Q'):
                    return False
                i -= 1
                j += 1

            return True

        def placeQueen(row):

            if(row == len(chess)):
                ans.append(chess[:])
                return

            for col in range(len(chess)):

                if(isSafe(row, col)):

                    # if i can place a queen then check for other n-row-1 queen
                    temp = chess[row]
                    chess[row] = chess[row][:col] + 'Q' + chess[row][col+1:]
                    # i cant place a queen in same row again so inc the row with 1

                    # we are not returning from here since we want
                    placeQueen(row+1)
                    # other solutions as well

                    chess[row] = temp

        placeQueen(0)
        return ans
