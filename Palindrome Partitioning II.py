# Qus:https://leetcode.com/problems/palindrome-partitioning-ii/
# understood by pepcoding. gap method + defination of palindrom abc if a==c then our ans is isPalin(b)

# Recursive solution (TLE) # we can optimise a bit by using a isPalindrom map (construct using gap method)
import sys


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


# easy intution using recursion

# ****** gap stategy ******

# given a string. find whether the given substring from i,j is palindrom or not
# dp[i][j] stores ans of string starting from index i to index j

# Note : We can store ans of reverse string just dp[i][j] = d[j][j] in case of palindrome
# for other cases we genrally not fill those but if we store those cells that means it will store ans of greate index to smaller index ans

# Note : Here dp[i][j] depends on dp[i+1][j-1] , hence we need to compute value of i+1 row value and col -1 value first
# so we need to create a loop from last to first index and col index from first to last


def createIsPalindromDp(s):
    n = len(s)

    dp = [[2]*n for _ in range(n)]

    for i in range(n-1, -1, -1):
        # print "row ", i
        for j in range(i, n):
            gap = j-i
            # print gap

            if(gap == 0):
                # only one character - always palindrom
                dp[i][j] = 1
            elif(gap == 1):
                # two characters - check if first and last char is same
                if(s[i] == s[j]):
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                # print i, j, s[i], s[j], dp[i+1][j-1]
                dp[i][j] = 1 if (s[i] == s[j] and dp[i+1][j-1]) else 0
    return dp


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        isPalin = createIsPalindromDp(s)

        d = [-1]*n

        def findMinCut(i, n):  # stores ans of suffix s[0..n-1]

            if(d[i] != -1):
                return d[i]

            minCut = sys.maxsize

            for j in range(i, n):
                # make a cut after i..j |)
                if(isPalin[i][j] and j == n-1):
                    # if palin then we can make a cut next to the last element
                    minCut = 0
                elif(isPalin[i][j]):
                    minCut = min(minCut, 1+findMinCut(j+1, n))

            d[i] = minCut

            return d[i]

        return findMinCut(0, n)
