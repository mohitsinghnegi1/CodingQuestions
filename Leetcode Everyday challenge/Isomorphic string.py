# Qus:https://leetcode.com/problems/isomorphic-strings/
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        r = {}

        for i in range(len(s)):
            if(s[i] in d and t[i] in r):

                if(d[s[i]] != t[i] or r[t[i]] != s[i]):
                    return False
            elif(s[i] not in d and t[i] not in r):
                d[s[i]] = t[i]
                r[t[i]] = s[i]
            else:
                return False

        return True
