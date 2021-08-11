# Qus:https://leetcode.com/problems/flip-string-to-monotone-increasing/

import sys


class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        Intution : let assume i be the index from where 1's is followed
        Ex : "00110"
        # time complexity O(n)
        """

        n = len(s)  # 5
        totalOne = s.count('1')  # 2

        prefixSum = 0
        min1 = sys.maxsize
        beforeOnes = 0

        for i in range(n):  # 0

            # total 1 till now
            # after zero = Space After - (total number of 1 - totalNumber of 1 before)
            # 5 - 1 - (2 - 0) #3 #2
            afterZero = n - i - (totalOne - beforeOnes)

            min1 = min(min1, beforeOnes+afterZero)  # 3

            beforeOnes += 1 if s[i] == '1' else 0  # 0

        min1 = min(min1, beforeOnes+0)
        return min1
