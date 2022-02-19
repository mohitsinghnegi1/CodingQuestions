# Qus: https: // leetcode.com/problems/palindromic-substrings/
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 0):
            return 0

        def palin(s, i, j):

            count = 0
            n = len(s)
            while(i >= 0 and j < n and s[i] == s[j]):
                count += 1
                i -= 1
                j += 1
            return count

        i = 0
        tPalin = 0
        n = len(s)

        #for every i there are two possible centers either i or either i and i+1
        while(i+1 < n):
            #this will give us count of all the palindrom whose center is i
            tPalin += palin(s, i, i)
            #this will give us count of all the palindrom whose center is i and i+1
            tPalin += palin(s, i, i+1)
            i += 1

        tPalin += palin(s, i, i)

        return tPalin
