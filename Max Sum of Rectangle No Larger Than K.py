# Qus:https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3801/

# tle O(6)
import sys


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        d = {}

        def getSum(r1, r2, c1, c2, matrix):

            sum1 = 0
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    sum1 += matrix[i][j]
            return sum1

        n = len(matrix)
        if(n == 0):
            return 0
        m = len(matrix[0])

        closest = -sys.maxsize

        for r2 in range(n):  # end row
            for c2 in range(m):  # end col

                for r1 in range(0, r2+1):
                    for c1 in range(0, c2+1):
                        sum1 = getSum(r1, r2, c1, c2, matrix)
                        if(sum1 <= k and sum1 > closest):
                            closest = sum1
        return closest


# time complexity O(n**5)


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        def getSum(r1, r2, c1, c2, matrix, prefix):

            sum1 = 0
            for i in range(r1, r2+1):

                # current row = i
                sum1 += prefix[i][c2]-(prefix[i][c1-1] if c1-1 >= 0 else 0)

                # for j in range(c1,c2+1):
                #     sum1 += matrix[i][j]
            return sum1

        n = len(matrix)
        if(n == 0):
            return 0
        m = len(matrix[0])

        closest = -sys.maxsize

        prefix = []
        for i in range(n):
            v = [matrix[i][0]]
            for j in range(1, m):
                v.append(v[-1]+matrix[i][j])
            prefix.append(v)
        # print prefix

        for r1 in range(n):  # end row
            for c1 in range(m):  # end col

                for r2 in range(r1, n):
                    for c2 in range(c1, m):
                        sum1 = getSum(r1, r2, c1, c2, matrix, prefix)
                        if(sum1 <= k and sum1 > closest):
                            closest = sum1
        return closest
