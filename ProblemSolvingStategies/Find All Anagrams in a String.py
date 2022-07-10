# O(N*26) time complexity
# just use the frequency array and compare, Anagram we can use this freq array concept
# Qus: https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """



        n = len(s)
        m = len(p)
        out = []

        if(n<m):
            return out

        a = [0]*26 # freq of s
        b = [0]*26 # freq of p


        for i in range(m):
            a[ord(s[i])-97]+=1
            b[ord(p[i])-97]+=1

        if(a==b):
            out.append(0)


        for i in range(m,n):
            a[ord(s[i])-97]+=1
            a[ord(s[i-m])-97]-=1

            if(a==b):
                out.append(i-m+1)

        return out


