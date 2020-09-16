# Qus: https: // leetcode.com/problems/partition-labels/


class Solution(object):
    def partitionLabels(self, s):
        """
        :type S: str
        :rtype: List[int]
        """
        if(len(s) == 0):
            return []

        d = {}

        #build a dictionary such that key will be the char and value will be its last index
        for i in range(len(s)):
            d[s[i]] = i

        #print d
        f = 0
        l = 0

        #approach
        #1) maintain 2 var to store start and max last position of elements visited till now                 #triverse through the string & keep updating last
        #2) once you reach the position which is greater then the Last then append
        #3) len (l-f) it into out & update first and last
        #4) Once the loop end also push the len (ie l-f+1)

        out = []
        for i in range(len(s)):

            if(i <= l):
                if(d[s[i]] > l):
                    l = d[s[i]]
            else:

                out.append(i-f)

                f = i
                l = d[s[i]]

        out.append(i-f+1)
        return out
