# QUs:https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3817/

# O(n**3) solution using dp TLE 108/118
class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # dp[i,j] --> binary value of i to j
        # dp[i,j] = 2**(i-j)*arr[i] + dp[i-1,j]
        # base case where i==j return arr[i]
        d = {}

        def toBin(arr, i, j):
            # base case
            if(i == j):
                return arr[j]

            if((i, j) in d):
                return d[(i, j)]

            d[(i, j)] = 2**(i-j)*arr[i] + toBin(arr, i+1, j)

            return d[(i, j)]

        n = len(arr)

        for end1 in range(1, n-1):
            val1 = toBin(arr, 0, end1-1)
            for end2 in range(end1+1, n):

                val2 = toBin(arr, end1, end2-1)
                val3 = toBin(arr, end2, n-1)

                if(val1 == val2 == val3):
                    return [end1-1, end2]

        return [-1, -1]


# O(n**3) solution TLE 108/118 tewst cases passed
class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        def isSameBinaryVal(arr, end1, end2):
            n = len(arr)
            i, j, k = end1-1, end2-1, n-1
            while(i >= 0 and j >= end1 and k >= end2):
                if(arr[i] != arr[j] or arr[j] != arr[k]):
                    return False
                i -= 1
                j -= 1
                k -= 1

            while(i >= 0):
                if(arr[i] != 0):
                    return False
                i -= 1

            while(j >= end1):
                if(arr[j] != 0):
                    return False
                j -= 1

            while(k >= end2):
                if(arr[k] != 0):
                    return False
                k -= 1

            return True

        n = len(arr)

        for end1 in range(1, n-1):
            for end2 in range(end1+1, n):

                if(isSameBinaryVal(arr, end1, end2)):
                    return [end1-1, end2]

        return [-1, -1]
