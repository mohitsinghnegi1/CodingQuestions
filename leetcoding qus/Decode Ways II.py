# Qus:https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3809/
# Timecomplexity : O(n)

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #   *1   9+2
        # 11 21 31 41 51 61 71 81 91
        # AA BA
        # K  ?
        # corner case ** ans 96

        s = "00"+s
        n = len(s)
        dp = [0]*(n)
        dp[1] = 1
        dp[0] = 1
        MOD = 10**9+7
        for i in range(2, n):

            # handle single digit
            if(s[i] == '*'):
                dp[i] = (dp[i-1]*9) % MOD
            elif(s[i] != '0'):
                dp[i] = dp[i-1]

            # handle two digit
            if(s[i-1] == "*" and s[i] == '*'):
                dp[i] = (dp[i] + dp[i-2]*15) % MOD
            elif(s[i-1] == '*'):
                # s[i] = 1,2,3,4,5,6,7,8,9
                # 1,2
                if(int(s[i]) <= 6):
                    dp[i] = (dp[i] + dp[i-2]*2) % MOD
                else:
                    dp[i] += dp[i-2]

            elif(s[i] == '*'):

                if(s[i-1] == '1'):
                    dp[i] = (dp[i] + dp[i-2]*9) % MOD
                elif(s[i-1] == '2'):
                    dp[i] += dp[i-2]*6
            else:
                # as old no *
                if(10 <= int(s[i-1:i+1]) <= 26):
                    dp[i] += dp[i-2]
        # print dp
        return dp[-1] % (MOD)

        # **  1 2    9+6
        # 1 = 9 ways
        # 2 = 81+ 15
