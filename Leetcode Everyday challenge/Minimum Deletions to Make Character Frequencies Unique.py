# Qus:https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# Time complexity : nlogn


import sys

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """

        freq = {}


        for i in s:
            freq[i] = freq.get(i,0) + 1



        f = list(freq.values())


        f.sort(reverse=True)

        maxFreq = sys.maxsize
        delete_count = 0

        for i in range(len(f)):


            if(f[i]>maxFreq):
                delete_count+= (f[i] - maxFreq)
                f[i] = maxFreq

                if(f[i]>0):
                    maxFreq -= 1
            else:

                maxFreq = f[i] - 1

        return delete_count