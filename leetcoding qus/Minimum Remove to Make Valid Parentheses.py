# Qus:https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# O(N) time complexity and O(N) space
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        count = 0
        stack = []
        ns = ''
        for i in range(len(s)):

            if(s[i] == '('):
                stack.append(i)
                # print stack,"1"
            elif(s[i] == ')'):
                if(stack == []):

                    stack.append(i)
                    # print stack,"2"
                else:
                    if(s[stack[-1]] == ')'):
                        stack.append(i)
                        # print stack,"3"
                    else:
                        # print stack,"3.5"
                        stack.pop()
                        # print stack,"4"

        # print stack
        out = ''
        j = 0
        for i in range(len(s)):
            if(j < len(stack) and stack[j] == i):
                j += 1
                continue
            out += s[i]
        return out
