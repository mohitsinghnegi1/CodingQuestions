# Qus:https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
from collections import Counter


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        def getResidualString(s, k):
            '''
                Intution : stack can be used to keep track how many dublicate at the top
                it will work even when we remove the top dublicate elements (Full proof)


            '''
            stack = []
            i = 0
            while(i < len(s)):
                # if stack is empty then add item to stack else check if top elent is same
                # if yes then increemnt the count and check if it is equal to k
                # if yes then pop else do nothing
                if(stack != [] and stack[-1][0] == s[i]):
                    stack[-1][1] += 1
                    if(stack[-1][1] >= k):
                        stack.pop()

                else:
                    # incase stack top elemt is not same then just append new element into stack
                    stack.append([s[i], 1])
                i += 1

            # return then left out elements
            out = ''
            for val, i in stack:
                out += val*i
            return out

        return getResidualString(s, k)
