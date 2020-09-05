# QUs: https: // leetcode.com/problems/search-a-2d-matrix/

# search based on index
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix) == 0):
            return False

        # since matrix is sorted we can apply binary search in this matrix

        n = len(matrix)
        m = len(matrix[0])
        l = 0

        r = n*m

        while(l < r):
            # calculate mid
            mid = (l+r)/2

            # cal row col based on mid
            row = mid/m
            col = mid % m

            if(matrix[row][col] == target):
                return True
            elif(matrix[row][col] < target):
                l = mid+1
            else:
                r = mid

        return False

# ---------------------------------------------------


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return False
        # sol 2 based on row and col binary search

        def binarySearch(row):

            l = 0
            r = len(matrix[row])

            while(l < r):
                mid = (l+r)/2

                if(matrix[row][mid] == target):
                    return True

                elif(matrix[row][mid] < target):
                    l = mid+1

                else:
                    r = mid

            return False

        t = 0
        b = len(matrix)

        while(t < b):
            mid = (t+b)/2

            if(target >= matrix[mid][0] and target <= matrix[mid][-1]):
                return binarySearch(mid)
            elif(target > matrix[mid][-1]):
                t = mid+1
            else:
                b = mid
        return False
