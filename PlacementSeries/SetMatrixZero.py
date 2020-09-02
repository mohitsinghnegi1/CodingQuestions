
# Qus:https://leetcode.com/problems/set-matrix-zeroes/

# --this solution is using extra O(n+m) space
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # with using O(n+m) space

        r = set()
        c = set()

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == 0):
                    r.add(i)
                    c.add(j)

        for i in range(n):
            for j in range(m):
                # if any of cur row or col in r or c respectively then make that                     #elemnt zero
                if(i in r or j in c):
                    matrix[i][j] = 0

        # print matrix


# solution 2 without using extra space
# solution with constant space and O(n*m*(n+m)) time complexity
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        def expend(i, j, d=None):

            if(i < 0 or i >= n or j < 0 or j >= m):
                return
            # dont override elemnt which is already 0 as we also
            # need to make its row and col elemnts zero
            if(matrix[i][j] != 0):
                # set that position with the val which is not possible for this                       #matrix
                matrix[i][j] = None

            if(d == None):
                # direct are like left,bottom,right,top (1,2,3,4)
                expend(i, j-1, 1)
                expend(i, j+1, 3)
                expend(i-1, j, 4)
                expend(i+1, j, 2)
            elif(d == 1):
                # expend in left direction
                expend(i, j-1, 1)
            elif(d == 3):
                # expend in right direction
                expend(i, j+1, 3)
            elif(d == 2):
                # expend in bottom direction
                expend(i+1, j, 2)
            else:
                # expend in top direction
                expend(i-1, j, 4)

        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == 0):
                    expend(i, j)
        #print matrix
        # turn all the none value as 0
        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == None):
                    matrix[i][j] = 0


# optimize it further to O(n*m)

# solution with constant space and O(n*m*(n+m)) time complexity
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        # we are using this variable because for first row and col
        # there is only one pos so we will use this new variable to store first col
        # True if need first col updation
        col1 = False

        # update first row and first col for respective cell if any of matrix[i][j]==0

        for i in range(n):

            # update col1 value if first column cell value is 0
            if(matrix[i][0] == 0):
                col1 = True

            for j in range(1, m):
                if(matrix[i][j] == 0):
                    matrix[i][0] = matrix[0][j] = 0

        # update row value based on first cell or col
        # if first row or col is 0 then update that cell value to 0

        for i in range(1, n):

            for j in range(1, m):
                if(matrix[i][0] == 0 or matrix[0][j] == 0):

                    matrix[i][j] = 0

        # handle first row
        if(matrix[0][0] == 0):
            for j in range(m):
                matrix[0][j] = 0

        # hande first col
        if(col1):
            for i in range(n):
                matrix[i][0] = 0
