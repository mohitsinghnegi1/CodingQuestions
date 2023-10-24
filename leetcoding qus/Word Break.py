# Qus:https://leetcode.com/problems/word-break/

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        #         dp = {}

        #         def solve(i):

        #             if(i==len(s)):
        #                 return True

        #             if(i in dp):
        #                 return dp[i]

        #             ans = False
        #             for k in range(i+1,len(s)+1):

        #                 if(s[i:k] in wordDict):
        #                     ans = solve(k)
        #                     if(ans==True):
        #                         dp[i] = ans
        #                         return ans

        #             dp[i]=False
        #             return dp[i]

        #         return solve(0)

        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            ans = False
            for k in range(i + 1, len(s) + 1):

                if (s[i:k] in wordDict):
                    ans = dp[k]
                    if (ans == True):
                        dp[i] = ans
                        break

            dp[i] = ans

        return dp[0]



