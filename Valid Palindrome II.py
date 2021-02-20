# QUs:https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(s == s[::-1]):
            return True

        def isPalin(s):
            n = len(s)-1
            for i in range(len(s)/2):
                if(s[i] != s[n-i]):
                    return False
            return True

        ns = s[::-1]

        for i in range(len(s)):
            if(s[i] != ns[i]):

                fs = s[:i]+s[i+1:]
                ss = ns[:i]+ns[i+1:]

                return isPalin(fs) or isPalin(ss)
