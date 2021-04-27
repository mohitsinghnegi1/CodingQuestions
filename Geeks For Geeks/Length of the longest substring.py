# Qus:https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1

"""
    Intution just keep track of the index of visited character also the window start and end index
    and see if char not in dict or if it is then it should not be in the current window
    keep tracking the size of window
"""


# User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, s):
        # code here
        d = {}
        max_so_far = 0
        max1 = 0
        start = 0
        for end in range(len(s)):
            if(s[end] not in d or (s[end] in d and d[s[end]] < start)):
                d[s[end]] = end
                max_so_far = max(max_so_far, end - start + 1)
            else:
                start = d[s[end]] + 1
                d[s[end]] = end

        return max_so_far


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()

        ob = Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends
