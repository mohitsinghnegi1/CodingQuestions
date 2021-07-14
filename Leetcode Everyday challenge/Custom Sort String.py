# Qus:https://leetcode.com/problems/custom-sort-string/
class Solution(object):
    def customSortString(self, order, str):
        """
        :type order: str
        :type str: str
        :rtype: str
        """
        # second approach

        count = [0]*26
        for i in str:
            count[ord(i)-97] += 1
        print count
        out = ""
        for i in order:
            out += i*count[ord(i)-97]
            print out

        print out
        for i in str:
            if(i not in order):
                out += i

        return out


#         first approach
#         a = [0]*26

#         for i in range(len(order)):
#             a[ord(order[i]) - 97] = i

#         b = list(str)
#         b.sort(key = lambda x:a[ord(x)-97])
#         print b
#         return "".join(b)
