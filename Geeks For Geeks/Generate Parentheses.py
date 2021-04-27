# Qus:https://practice.geeksforgeeks.org/problems/generate-all-possible-parentheses/1#
# User function Template for python3

class Solution:
    def AllParenthesis(self, n):

        out = []

        def printParenthesis(n, l, r, s):
            # print(l,r)
            if(r > l):
                return

            if(l == n and r == n):
                # print(s)
                out.append(s)
                return

            if(l < n):
                printParenthesis(n, l+1, r, s+'(')
            if(r < l):
                printParenthesis(n, l, r+1, s+')')

        printParenthesis(n, 0, 0, '')
        # print(out)
        return out


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        n = int(input())
        ob = Solution()
        result = ob.AllParenthesis(n)
        result.sort()
        for i in range(0, len(result)):
            print(result[i])


# } Driver Code Ends
