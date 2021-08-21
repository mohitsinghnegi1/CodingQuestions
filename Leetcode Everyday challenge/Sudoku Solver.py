# QUs:https://leetcode.com/problems/sudoku-solver/
# tag backtracking
# remember you can't pass  col to continue from same point but we still pass row and start the next recursion from same row to optimise
# https://www.youtube.com/watch?v=FWAIf_EVUKE
def isValid(board, row, col, c):

    startRow = row/3
    startCol = col/3

    for i in range(9):
        if(board[i][col] == c):
            return False

        if(board[row][i] == c):
            return False

        cc = startCol*3 + i % 3
        rr = startRow*3 + i/3
        if(board[rr][cc] == c):
            return False

    return True


def solve(board, n, m, r):
    # print "new", r,c,board

    for i in range(r, n):
        for j in range(0, m):
            if(board[i][j] == '.'):
                # in case of empty cell try to insert every possible number from 1 to 9

                for num in range(1, 10):
                    c = str(num)
                    if(isValid(board, i, j, c)):
                        # print "isValid"
                        board[i][j] = c
                        # print board
                        if(solve(board, n, m, i)):  # is this number valid
                            # print "is solvable",i,j,c
                            return True

                        board[i][j] = '.'
                        # print "not solvable",board

                return False

        # print i

    return True


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        solve(board, n, m, 0)
