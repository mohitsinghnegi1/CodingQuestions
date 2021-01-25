# Qus:https://leetcode.com/problems/greatest-common-divisor-of-strings/

# fastest then 100% O(n) time complexity
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # always assume x is greater
        def gcd(x, y):
            if(y == 0):
                return x
            # keep smaller ie (2nd arg) in frond and lower then 2nd argument ie x%y
            return gcd(y, x % y)

        len1 = gcd(len(str1), len(str2))

        n = len(str1)/len1
        m = len(str2)/len1

        t1 = str1[:len1]
        t2 = str2[:len1]

        # if all three condition are true ie t1 == t2 and t1*m ==str1 and t2*n == str2
        # then return t1 else return ''
        if(t1 == t2 and t1*n == str1 and t2*m == str2):
            return t1

        return ""
