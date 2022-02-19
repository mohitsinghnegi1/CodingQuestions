

# QUs:https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# -----Recursive solution


def getFull(left, string):
    out = []
    for right in string:
        out.append(left+right)
    return out


def getCombinations(digits, d):
    # handle case when we get a combination and ther is no digit left fo
    # generating combination
    if(digits == ''):
        return ['']

    out = []

    for c in d[digits[0]]:
        # add all combination which start from char c and
        # combine it with all combination possible with digits[1:] string
        a = getFull(c, getCombinations(digits[1:], d))
        out.extend(a)
    return out


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # if digit is empty there is no combination
        if(digits == ''):
            return []

        d = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # this function will return list of combination
        return getCombinations(digits, d)

    # -------iterative solution


class Solution2(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # if digit is empty there is no combination
        if(digits == ''):
            return []

        d = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        out = ['']

        for digit in digits:

            out1 = []
            for cr in d[digit]:

                # till now we have sub_comb we need to combine it with
                # new cr mapped with digit

                for k, sub_comb in enumerate(out):
                    # print "out[k]",out[k]
                    out1.append(out[k]+cr)
                # print out1
            out = out1
        return out

       # recursive solution new


class Solution3(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        """
        Intution :
        for all element in stack suffix each elemnt with digits[i]
        
        stack = [""]
        
        ex 23
        for 2 : abc
        1. "a" , "b" ,"c"
        
        for 3
        new stack now ["a" , "b" ,"c"]
        1. ad , ae, af,bd,be,bf,cd,ce,cf
        new stack now : [ad , ae, af,bd,be,bf,cd,ce,cf]
        
        
        
        
        """

        if(digits == ""):
            return []

        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        stack = [""]

        def combine(digits, stack):

            if(digits == ""):
                return []

            chars = d[digits[0]]
            v = []

            while(stack):
                node = stack.pop()

                for char in chars:
                    v.append(node+char)
            stack.extend(v)
            combine(digits[1:], stack)

        combine(digits, stack)

        return stack
