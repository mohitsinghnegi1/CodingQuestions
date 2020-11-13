# QUs:https://leetcode.com/problems/decode-string/

def getMulFactor(stack):
    mul = ''
    while(stack and stack[-1].isdigit()):
        mul += stack.pop()
    return int(mul[::-1])


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # intution if we get ']' then pop until we get a number , then multiply and push         # back to stack

        stack = []
        i = 0

        while(i < len(s)):
            if(s[i] == ']'):
                temp = ''
                while(not stack[-1] == '['):
                    # very important , this is differnt then                           #reversing string at the end ,
                    temp = stack.pop()+temp
                    # as we have cases where stack elemnt is string not char
                stack.pop()
                # Note number could be of two digit or more
                mul = getMulFactor(stack)
                stack.append(mul*temp)
            else:
                stack.append(s[i])

            i += 1

        out = ''
        for str1 in stack:
            out += str1

        return out
