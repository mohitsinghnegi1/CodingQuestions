# Qus:https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # iterative solution
        if(numRows == 0):
            return []
        if(numRows == 1):
            return [[1]]
        if(numRows == 2):
            return [[1], [1, 1]]

        out = [[1], [1, 1]]

        for i in range(2, numRows):
            v = []
            for j in range(i+1):
                #print i,j
                # assing top and top left sum  to current cell
                # check the boundary conditions
                el = out[i-1][j] if j < i else 0
                el += out[i-1][j-1] if j-1 >= 0 else 0
                v.append(el)
            out.append(v)

        return out
