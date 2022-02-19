# Qus:https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(stack, out):

            rev = ''
            while(stack[-1] != '('):
                rev += stack.pop()
            stack.pop()
            return rev

        stack = []

        i = 0
        out = ''
        while(i < len(s)):
            if(s[i] == '('):
                stack.append(s[i])
            elif(s[i] == ')'):
                rev = reverse(stack, out)
                # don't push the entire string it will lead to wrong ans
                stack.extend(list(rev))
            else:
                stack.append(s[i])
            i += 1

        return "".join(stack)
