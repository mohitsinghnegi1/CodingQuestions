# Qus:https://leetcode.com/problems/palindrome-partitioning-ii/
# understood by pepcoding. gap method + defination of palindrom abc if a==c then our ans is isPalin(b)

# Recursive solution (TLE) # we can optimise a bit by using a isPalindrom map (construct using gap method)
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # code here
        if(s == s[::-1]):
            return 0

        min_cut = sys.maxsize

        for i in range(1, len(s)+1):

            if(s[:i] == s[:i][::-1]):
                # palindorm
                min_cut = min(min_cut, 1 + self.minCut(s[i:]))

        return min_cut


# solution using ispalin gap method to find is palin or not
def constructPalinMatrix(s):

    pm = [[False for i in range(len(s))] for _ in range(len(s))]

    for gap in range(len(s)):

        for i in range(len(s)-gap):
            # print i,gap
            if(gap == 0):
                pm[i][i + gap] = True
            elif(gap == 1):
                if(s[i] == s[i + gap]):
                    pm[i][i + gap] = True
                else:
                    pm[i][i + gap] = False
            else:
                if(s[i] == s[i + gap]):
                    pm[i][i + gap] = pm[i+1][i + gap-1]
                    # print i,gap
                else:
                    pm[i][i + gap] = False
    return pm


class Solution2(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        pm = constructPalinMatrix(s)

        def findMinCut(s, st, end):

            if(st >= end):
                return 0
            if(pm[st][end] == True):
                return 0

            min_cut = sys.maxsize

            for i in range(st+1, end+1):

                if(pm[st][i-1]):
                    # palindorm
                    min_cut = min(min_cut, 1 + findMinCut(s, i, end))

            return min_cut

        return findMinCut(s, 0, len(s)-1)

# optimized method O(N**2)


def constructPalinMatrix(s):

    pm = [[False for i in range(len(s))] for _ in range(len(s))]

    for gap in range(len(s)):
        for i in range(len(s)-gap):

            if(gap == 0):
                pm[i][i + gap] = True
            elif(gap == 1):
                if(s[i] == s[i + gap]):
                    pm[i][i + gap] = True
            else:
                if(s[i] == s[i + gap]):
                    pm[i][i + gap] = pm[i+1][i + gap-1]
    return pm


class Solution3(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        pm = constructPalinMatrix(s)

        def findMinCut(s):

            if(len(s) <= 1):
                return 0

            dp = [sys.maxsize]*len(s)  # use suffix method to find min cut

            dp[0] = 0  # how many cuts are required to find prefix of len i+1
            # if we have one len string then the min cut will be alway zero
            dp[1] = 0 if(s[0] == s[1]) else 1

            for end in range(2, len(s)):

                if(pm[0][end] == True):
                    dp[end] = 0
                else:

                    for start in range(1, end+1):

                        if(pm[start][end] == True):
                            dp[end] = min(dp[end], 1+dp[start-1])

            return dp[-1]

        return findMinCut(s)
