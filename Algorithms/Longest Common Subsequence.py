# Qus:https://leetcode.com/problems/longest-common-subsequence/

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        text1 = " "+text1
        text2 = " "+text2
        # d[i][j] = suppose we have first i char of text1 and first j char of text2 -> find lcs
        d = [[0 for j in range(len(text2))] for i in range(len(text1))]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if(text1[i] == text2[j]):
                    d[i][j] = 1+d[i-1][j-1]
                else:
                    d[i][j] = max(d[i-1][j], d[i][j-1])
        return d[-1][-1]
