# Qus: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

from collections import defaultdict


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        # intution (a + b)%60 = 0
        #           (a % 60 + b % 60) % 60 = 0
        #           (x + y) % 60 = 0  where x and y < 60 for sure
        # since 1 <= time[i] <= 500    we can assure a canot be 0 without modulo

        count = 0

        for a in time:
            x = a % 60
            if (60 - x) % 60 in d:
                # let say a was 60 and x = a % 60 =0    60 - x = 60 will
                count += d[(60 - x) % 60]
                # not be in dict for sure , so we take % of it
            d[x] += 1

        # print d
        return count
