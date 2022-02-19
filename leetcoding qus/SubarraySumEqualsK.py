# Qus:https://leetcode.com/problems/subarray-sum-equals-k/
from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, target):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        d = defaultdict(int)
        d[0] = 1

        runningSum = 0
        count = 0

        for val in nums:
            runningSum += val
            if d.get(runningSum-target, None) != None:
                count += d[runningSum-target]
            # print d

            d[runningSum] += 1

        # nums=[9,0,0] target=9 d={0:1}
        # 1)  val=9 rS=9  runningSum-target=0 count=1 d={0:1,9:1}
        # 2)  val=0 rS=9  runningSum-target=0 count=1+d[0]=2 d={0:1,9:2}
        # 3)  val=0 rS=9  runningSum-target=0 count=2+d[0]=3 d={0:1,9:3}

        #    nums=[9,9,9] target=9 d={0:1}
        # 1) val=9 rS=9  runningSum-target=0 count=1 d={0:1,9:1}
        # 2) val=9 rs=18 runningSum-target=9 count=count+d[9]=2 d={0:1,9:1:18:1}
        # 3) val=9 rs=27 runningSum-target=18 count=2+d[18]=3  d={0:1,9:1:18:1,27:1}

        return count
