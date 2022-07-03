# Qus: https://leetcode.com/problems/wiggle-subsequence/
# time complexity : O(N**2)
# space : O(N)

# try to optimise it to O(N) and O(1) space


class Node:
    def __init__(self,val):
        self.val = val
        self.isPositive = False # first nuber can be be pos or neg
        self.isNegative = False # first nuber can be be pos or neg
        self.maxLengthPos = 1
        self.maxLengthNeg = 1

    def __str__(self):

        return " "+str(self.val)+" "+str(self.isPositive)+" "+str(self.isNegative)+" "+str(self.maxLengthPos)+" "+str(self.maxLengthNeg)


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max positive , max -ve
        # -ve or pos  == if number is smaller and -ve then we can assume current eleemnt as pos
        # if prev number is positive and bigger then current number the we can assumume current number as negative
        # first number as length 1
        # last possitve and last negative we need to find ? do we need to find every time ? no because wrt current number

        n = len(nums)

        # if(n<3):
        #     return n


        max_so_far = 1

        dp = []

        for i in range(n):

            curNumber = nums[i]

            node = Node(curNumber)

            if(i==0):
                node.isPositive = True
                node.isNegative = True

            for j in range(i-1,-1,-1):

                prevNode = dp[j]

                if(prevNode.val < curNumber and prevNode.isNegative ):


                    if(1+prevNode.maxLengthNeg >= node.maxLengthPos):
                        node.isPositive = True
                        node.maxLengthPos = 1+prevNode.maxLengthNeg



                if(prevNode.val > curNumber and prevNode.isPositive):
                    # node.maxLength = max(node.maxLength,1+prevNode.maxLength)
                    if(1+prevNode.maxLengthPos >= node.maxLengthNeg):
                        node.isNegative = True
                        node.maxLengthNeg = 1+prevNode.maxLengthPos


            max_so_far =  max(max_so_far,node.maxLengthPos,node.maxLengthNeg)
            # print node
            dp.append(node)


        return max_so_far