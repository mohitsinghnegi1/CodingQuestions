# Qus:https://leetcode.com/problems/reorganize-string/
# Time complexity is O(n)

from heapq import heappush, heappop
from collections import defaultdict


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)

        # as per my Observation if there is odd number of char then the
        maxlimit = (((n/2)+1) if(n % 2) else n/2)
        # max possible repeatition of a partical char at max len(S)/2+1 and for odd len string it is len(S)/2

        # print maxlimit

        # find the frequency of every char in the string
        d = defaultdict(int)
        for char in S:
            d[char] += 1
            # if it exceed the max limit then return ""
            if(d[char] > maxlimit):
                return ""

        # now we know that the string is possible
        # the Intution behind the resultant string is keep the max frequency char as as close as possible /more             # frequent following constrant

        # create a max heap
        heap = []

        for char in d:
            freq = d[char]
            # this is min heap so we need max frequency at top
            heappush(heap, (-freq, char))
            # so just reverse the sign

        o = ''

        while(heap):
            # find the most frequent char from the current heap
            freq, char = heappop(heap)
            o += char  # add that to the resultant string
            if(heap):
                # pop out second frequent char
                freq2, char2 = heappop(heap)
                o += char2  # add it to resultant string too
                if(freq+1 < 0):  # see if the frequency of these character is greater then 1 (here sign are reversed)
                    heappush(heap, (freq+1, char))
                if(freq2+1 < 0):
                    heappush(heap, (freq2+1, char2))

        return o
