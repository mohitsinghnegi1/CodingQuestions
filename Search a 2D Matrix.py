# Qus:https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = n*m

        while(l < r):
            mid = (l+r)/2

            row = mid/m  # we use % Cols to get a column
            col = mid % m  # we use / Cols to get a row

            if(matrix[row][col] == target):
                return True
            elif(matrix[row][col] < target):
                l = mid+1
            else:
                r = mid

        return False


class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        i = 0
        j = m-1

        # 2
        # qus when to increment i ? ans is when matrix[i][j] < target
        # when to decrement j

        while(i >= 0 and i < n and j >= 0 and j < m):

            if(target == matrix[i][j]):
                return True
            elif(target < matrix[i][j] and target >= matrix[i][0]):
                j -= 1
            else:
                i += 1

        return False
