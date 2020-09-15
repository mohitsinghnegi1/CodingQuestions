# QUs:https://leetcode.com/problems/maximal-square/

def sqr(matrix, ti, tj, bi, bj, n, m):

    # conditions for return
    if(bi > n or bj > m):
        return

    # conditions for max1
    for i in range(ti, bi):
        for j in range(tj, bj):
            if(matrix[i][j] != '1'):
                # print "->",ti,tj,bi,bj,i,j,matrix
                return
    global max1
    # if square then update max1
    max1 = max(max1, bi-ti)

    # subproblem
    sqr(matrix, ti, tj, bi+1, bj+1, n, m)


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return 0

        global max1
        max1 = 0

        n = len(matrix)
        m = len(matrix[0])

        # approach--
        # triverse in a matrix maintain a global max of maximum area square
        # for each cell check if it formaing a square if then  yes update max1
        # if it is not forming a square then return else expend the size diagonally
        # repeat the same process of calculating is current square is a valid square?
        # if yes then update max1 else return

        for i in range(n):
            for j in range(m):
                sqr(matrix, i, j, i+1, j+1, n, m)

        return max1*max1


# --O(n^3) approach using memorization


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # approach
        # each cell represent what is the max possible till (i,j) cell
        # so imagine if digonal left cell is of square of size 2 then cur squ can be of max size 3
        # using this logic we are reducing computation from n*n to 2*n

        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return 0

        n = len(matrix)
        m = len(matrix[0])

        # to keep track of max side of square
        max1 = 0

        for i in range(n):
            for j in range(m):

                if(matrix[i][j] == '1'):

                    # what is previous sqr value that is on digonally left
                    # handle corner case when there is only one element or single row or single col
                    prevSqrLength = matrix[i-1][j -
                                                1] if (i-1 >= 0 and j-1 >= 0) else '0'

                    # max steps to move in top or left direction
                    # please take care of the type conversion
                    mxSteps = int(prevSqrLength)

                    up = 0

                    for k in range(mxSteps+1):
                        if(matrix[i-k][j] != '0'):
                            up += 1
                        else:
                            # dont forgot to add break othervise it will give wrong ans
                            break

                    left = 0

                    for k in range(mxSteps+1):
                        if(matrix[i][j-k] != '0'):
                            left += 1
                        else:
                            break

                    # include itself also  and take min of both side as small side will tell what is the possible                     #square
                    maxPossibleSqrSide = min(up, left)

                    # store max possible value for later computations
                    matrix[i][j] = str(maxPossibleSqrSide)

                    max1 = max(max1, maxPossibleSqrSide)

        # return area
        return max1*max1


# ----optimized approach


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # approach
        # each cell represent what is the max possible till (i,j) cell
        # so imagine if digonal left cell is of square of size 2 then cur squ can be of max size 3
        # using this logic we are reducing computation from n*n to 2*n

        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return 0

        n = len(matrix)
        m = len(matrix[0])

        # to keep track of max side of square
        max1 = 0

        for i in range(n):
            for j in range(m):

                if(matrix[i][j] == '1'):

                    # try to visualize that max size of sqr will be left min(left,mid,top) value of computed matrix
                    # ie (i-1,j) , (i,j+1), (i-1,j-1) as all of them representing max size square up to (i,j)
                    up = int(matrix[i-1][j])+1 if i-1 >= 0 else 1

                    # what is previous sqr value that is on digonally left
                    # handle corner case when there is only one element or single row or single col
                    prevSqrLength = int(
                        matrix[i-1][j-1])+1 if (i-1 >= 0 and j-1 >= 0) else 1

                    left = int(matrix[i][j-1])+1 if j-1 >= 0 else 1

                    # include itself also  and take min of both side as small side will tell what is the possible                     #square
                    maxPossibleSqrSide = min(up, left, prevSqrLength)

                    # store max possible value for later computations
                    matrix[i][j] = str(maxPossibleSqrSide)

                    max1 = max(max1, maxPossibleSqrSide)

        # return area
        return max1*max1
