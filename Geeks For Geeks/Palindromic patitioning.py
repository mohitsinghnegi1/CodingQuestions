# Qus:https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1#


# brute force
# time complexity = n**h   where h is the hight of tree


# User function Template for python3
import sys


class Solution:
    def palindromicPartition(self, str):
        # code here
        if(str == str[::-1]):
            return 0

        min_cut = sys.maxsize

        for i in range(1, len(str)+1):

            if(str[:i] == str[:i][::-1]):
                # palindorm
                min_cut = min(min_cut, 1 + self.palindromicPartition(str[i:]))

        return min_cut


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input()

        ob = Solution()
        print(ob.palindromicPartition(str))
# } Driver Code Ends
