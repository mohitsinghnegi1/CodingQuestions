# Qus :https://leetcode.com/problems/minimum-window-substring/
# resource : https://www.youtube.com/watch?v=eS6PZLjoaq8


from collections import defaultdict
from collections import defaultdict, Counter
import sys


def validWindow(c1, c2):

    # complexity of validating a window is O(26)
    # since there are maximum 26 uppercase characters

    for i in c1:
        if(c1[i] > c2[i]):
            return False
    return True

# total complexity of this solution is
# Time complexity O(26*2*n)
# space complexity O(len(2t))


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # create two dict
        # one will store frequency of each character required in a window
        # c2 is a dict which will store frequency of chr present in cur window

        c1 = Counter(t)
        c2 = {}
        for i in c1:
            c2[i] = 0

        minlen = sys.maxsize
        o = ''
        # this l variable will be left pointer and i will be the right pointer
        l = 0

        for i in range(len(s)):

            # insert current elemnt in the c2 dict if key is present
            # since we have initialized c2 with the keys which we are required

            if(s[i] in c2):
                c2[s[i]] += 1

                # since we have added char in a dict c2
                # so may be this window contins whole character

                while(validWindow(c1, c2)):
                    if(i-l+1 < minlen):
                        minlen = i-l+1
                        o = s[l:i+1]

                        # we need to move left, means s[l] will not be available in c2
                    if(s[l] in c2):
                        c2[s[l]] -= 1

                    l += 1
        return o


# approach 2 more optimized


class Solution2(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        tfreq = defaultdict(int)
        sfreq = defaultdict(int)

        for char in t:
            tfreq[char] += 1

        s1 = []

        for i in range(len(s)):
            if(s[i] in tfreq):
                s1.append([i, s[i]])

        i = 0

        ans = (-sys.maxsize, sys.maxsize)

        def isValid(st, ed, count):
            if(ed-st) < len(t):
                return False

            for char in tfreq:

                if(count[char] < tfreq[char]):
                    return False

            return True

        for (j, (end, char)) in enumerate(s1):

            sfreq[char] += 1

            while(i < len(s1) and isValid(s1[i][0], s1[j][0]+1, sfreq)):

                if ((s1[j][0]+1) - s1[i][0]) < (ans[1]-ans[0]):
                    ans = (s1[i][0], s1[j][0]+1)

                sfreq[s1[i][1]] -= 1
                i += 1

        return s[ans[0]:ans[1]] if ans != (-sys.maxsize, sys.maxsize) else ""
