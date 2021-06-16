# Qus:https://leetcode.com/problems/sum-of-all-subset-xor-totals/

def solve(nums, i, xor, ans):
    # print xor
    if(i == len(nums)):
        ans[0] = ans[0]+xor
        # print xor
        return
    # take
    solve(nums, i+1, nums[i] ^ xor, ans)
    # dont take
    solve(nums, i+1, xor, ans)


class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [0]
        solve(nums, 0, 0, ans)
        return ans[0]
