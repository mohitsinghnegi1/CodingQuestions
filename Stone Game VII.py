# QUs:https://leetcode.com/problems/stone-game-vii/

"Brute force solution TLE "


class Solution1(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)

        ps = [stones[0]]
        for i in range(1, n):
            ps.append(ps[-1]+stones[i])

        def findDiff(i, j):
            # both will try to increase his score
            if(i == j):
                # if only one pile of stone left then he has to remove that tile and he
                # will not get any score
                return 0

            # if i remove left i will get right sum
            # if i remove right i get the left sum
            # i need to get the ans which will give overall greter ans
            # so lets get the range sums value using prefix sum
            rightSum = (ps[j]-ps[i])
            leftSum = ps[j-1] - (ps[i-1] if i-1 >= 0 else 0)
            return max(rightSum - findDiff(i+1, j), leftSum - findDiff(i, j-1))

        return findDiff(0, n-1)


"""
    This approach is also giving TLE 67/68 test passed
"""


class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)

        # let do memorization
        d = {}

        def findDiff(i, j, total):
            if((i, j) in d):
                return d[(i, j)]
            # both will try to increase his score
            if(i == j):
                # if only one pile of stone left then he has to remove that tile and he
                # will not get any score
                return 0

            # if i remove left i will get right sum
            # if i remove right i get the left sum
            # i need to get the ans which will give overall greter ans
            # so lets get the range sums value using prefix sum
            rightSum = total-stones[i]
            leftSum = total-stones[j]

            d[(i, j)] = max(rightSum - findDiff(i+1, j, rightSum),
                            leftSum - findDiff(i, j-1, leftSum))

            return d[(i, j)]

        # we keep on decreasing sum on every stone removal
        # also it will make easy to get left and right sum
        return findDiff(0, n-1, sum(stones))


# just little optimization from using a dict to array reduced the time complexity and no TLE
# TIme complexity O(N**2)

class Solution3(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)

        # let do memorization
        d = [[-1]*1002 for i in range(1002)]

        def findDiff(i, j, total):
            if(d[i][j] != -1):
                return d[i][j]
            # both will try to increase his score
            if(i == j):
                # if only one pile of stone left then he has to remove that tile and he
                # will not get any score
                return 0

            # if i remove left i will get right sum
            # if i remove right i get the left sum
            # i need to get the ans which will give overall greter ans
            # so lets get the range sums value using prefix sum
            rightSum = total-stones[i]
            leftSum = total-stones[j]

            d[i][j] = max(rightSum - findDiff(i+1, j, rightSum),
                          leftSum - findDiff(i, j-1, leftSum))

            return d[i][j]

        # we keep on decreasing sum on every stone removal
        # also it will make easy to get left and right sum

        return findDiff(0, n-1, sum(stones))
