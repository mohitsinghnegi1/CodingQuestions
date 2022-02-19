# Qus:https://leetcode.com/problems/candy/

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # out[i] = max continuous subsequence ending at i
        out = [1]
        for i in range(1, len(ratings)):
            if(ratings[i] > ratings[i-1]):
                out.append(out[-1]+1)
            else:
                out.append(1)

        # out2[i] is the max continuous subsequence ending at i from the right
        out2 = [1]*len(ratings)
        for i in range(len(ratings)-2, -1, -1):
            if(ratings[i] > ratings[i+1]):
                out2[i] += out2[i+1]
            else:
                out2[i] = 1

        # we know we need to take max out of both
        for i in range(0, len(ratings)):
            out[i] = max(out[i], out2[i])
        # print out
        return sum(out)
