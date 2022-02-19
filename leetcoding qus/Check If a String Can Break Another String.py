# Qus:https://leetcode.com/problems/check-if-a-string-can-break-another-string/

from collections import Counter


class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counters1 = Counter(s1)
        counters2 = Counter(s2)

        def check(c1, c2):
            s = 0
            for i in 'abcdefghijklmnopqrstuvwxyz'[::-1]:
                s += c1[i] - c2[i]
                if(s < 0):
                    return False
            return True

        print counters1, counters2
        return check(counters1, counters2) or check(counters2, counters1)
