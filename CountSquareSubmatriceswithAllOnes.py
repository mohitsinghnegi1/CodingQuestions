# Qus: https: // leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return 0

        count = 0

        # first row sum
        count += sum(matrix[0])

        for i in range(1, len(matrix)):
            # first column sum
            count += matrix[i][0]

            for j in range(1, len(matrix[0])):

                if(matrix[i][j] == 1):
                    # no of possible square that end at point i,j will
                    # be equal to the min of max possible square out of
                    # square ending at i-1,j-1 & i-1,j & i,j-1

                    matrix[i][j] = 1+min(matrix[i][j-1],
                                         matrix[i-1][j], matrix[i-1][j-1])
                    count += matrix[i][j]
        print matrix
        return count


# Follow below syntax to reduct one extra loop
# for (int i = 0; i < A.size(); ++i):
#     for (int j = 0; j < A[0].size(); res += A[i][j++]):
#         if (A[i][j] && i && j):
#             A[i][j] += min({A[i - 1][j - 1], A[i - 1][j], A[i][j - 1]});
