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

# using recursion and memorization


class Solution2(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Intution : if the current s have first char 0 then this the the invalid way of decoding
        
        if we are able to decode the string till string gets over then this is the valid way of decoding
        """

        # for memorization
        d = {}

        # this function will return number of ways a string can be decoded
        def getWays(s):

            # if we reach the end of string without any error then this is a valid decoding
            if(s == ""):
                return 1

            # in case we encounter first char of string as 0 that mean we can reach to end of string using proper
            # decoding
            if(s[0] == '0'):
                return 0

            # memo
            if(s in d):
                return d[s]

            # if first char is valid then we can move one step forward
            one = getWays(s[1:])
            two = 0

            # we can move two step forward if len is >=2 and first char is non zero and the s[:2] is less then 26
            if(len(s) >= 2 and int(s[:2]) >= 10 and int(s[:2]) <= 26):
                two = getWays(s[2:])

            # memo
            d[s] = one + two
            return d[s]

        return getWays(s)
