# Qus:https://practice.geeksforgeeks.org/problems/excel-sheet5448/1
# User function Template for python3
import math


class Solution:
    def ExcelColumn(self, N):
        # return required string
        # code here
        out = ""
        while(N):
            if(N % 26 == 0):
                out += "Z"
                N = (N//26 - 1)
            else:

                out += chr((N-1) % 26 + ord('A'))
                N = (N//26)

        return out[::-1]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        ob = Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends
