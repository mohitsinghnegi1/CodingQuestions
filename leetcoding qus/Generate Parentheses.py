# QUs:https://leetcode.com/problems/generate-parentheses/

# optimised solution of balanced parenthesis
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []

        def genPt(l, r, n, bP):

            if(l+r == 2*n):
                out.append(bP)
                return
            # we can insert up to n number of left
            if(l < n):
                genPt(l+1, r, n, bP+"(")

            # we can insert upto l numbers of right brackets
            if(r < n and r < l):
                genPt(l, r+1, n, bP+")")

            return

        l, r = 0, 0
        genPt(l, r, n, "")

        return out
