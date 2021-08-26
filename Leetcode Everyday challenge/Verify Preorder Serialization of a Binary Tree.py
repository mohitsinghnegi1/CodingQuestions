# Qus:https://leetcode.com/submissions/detail/316029641/

# time complexity O(n)
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        a = preorder.split(',')[::-1]

        if(len(a) == 1 and a[0] == '#'):
            return True

        stack = []

        while(a != []):

            el = a.pop()
            if(el == '#'):
                if(stack == []):
                    return False

                while(stack and stack[-1] == '#'):
                    stack.pop()
                    stack.pop()
                if(stack == []):
                    if(a == []):
                        return True
                    return False
                stack.append(el)

            else:
                stack.append(el)

            # print stack

        return len(stack) == 0


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        a = preorder.split(',')

        if(a[0] == '#'):  # special case when root is null
            if(len(a) == 1):
                return True
            return False

        slots = 1
        for i in range(len(a)):
            slots -= 1  # every node will consume one space
            if(slots < 0):
                return False  # any time if we found slot<0 we return False
            if(a[i] != '#'):
                slots += 2  # when current elemnt is not null that means there is two
                # more null slots

        return slots == 0
