# QUs:https://leetcode.com/problems/find-the-town-judge/

from collections import defaultdict


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # approach 2 (easy)

        in_deg = [0] * (N+1)
        out_deg = [0] * (N+1)

        for a, b in trust:
            out_deg[a] += 1
            in_deg[b] += 1

        for i in range(1, N+1):
            if in_deg[i] == N-1 and out_deg[i] == 0:
                return i

        return -1

#         # approach one
#         if(N==0):
#             return -1

#         d=defaultdict(set)

#         for person,trustperson in trust:
#             d[person].add(trustperson)

#         # check if there are n-1 person exactly who trust if not return -1
#         if(len(d.keys())!=N-1):
#             return -1

#         expectedJudge=None

#         for i in range(1,N+1):
#             if(i not in d):
#                 expectedJudge=i
#                 break

#         print expectedJudge

#         for key in d:
#             if(expectedJudge not in d[key]):
#                 return -1

#         return expectedJudge
