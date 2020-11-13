# qus:https://leetcode.com/problems/decode-ways/
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if(s[0] == '0'):
            # corner case 05 should return 0
            return 0

        dp = [0]*len(s)
        dp[0] = 1

        for i in range(1, len(s)):
            if(s[i] == '0'):
                if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                    # case 2201
                    # for '20' it should give 1
                    dp[i] = dp[i-2] if i-2 >= 0 else 1
                else:
                    return 0
            else:
                # since we are not just adding one more number to prev number
                # so number of possible ways to decode string is same as before
                dp[i] = dp[i-1]

                # if s[i-1:i+1]<=26 >=10  then we no we can reach this position
                # from s[i-2] so we are also adding that dp[i-2] to dp[i]
                if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                    dp[i] += dp[i-2] if i-2 >= 0 else 1
        return dp[-1]

        # solution analysis
        # when s[i]=='0'

        # understanding testcase
        # case  '66666' => output =1
        # explaination there is no possibilty of combining any two digit
        # to create a single number
        # Note dp[i] states that how many ways of decoding are possible
        # if we consider char upto i index
        # if we have s[i]=='0' then there is only one possiblity of creating
        # a correct decode string if s[i-1:i+1]<26 and >10 then it will be
        # equal to dp[i-2]
