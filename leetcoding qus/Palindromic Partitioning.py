# Ous: https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1

# User function Template for python3
import sys


class Solution:
    def palindromicPartition(self, text):
        # code here

        # d =  {}

        # def pp(i):

        #     if(i==len(text)):
        #         return 0

        #     if(i in d):
        #         return d[i]

        #     ans = sys.maxsize

        #     for k in range(i+1,len(text)+1):

        #         if(text[i:k]==text[i:k][::-1]):

        #             res = pp(k)
        #             if(res!=sys.maxsize):
        #                 ans = min(1 + res,ans) # not to return immediately as we need min cuts

        #     d[i] =  ans
        #     return d[i]

        # return pp(0)-1

        n = len(text)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            ans = sys.maxsize
            for k in range(i + 1, n + 1):

                if (text[i:k] == text[i:k][::-1]):

                    res = dp[k]
                    if (res != sys.maxsize):
                        ans = min(1 + res, ans)  # not to return immediately as we need min cuts

            dp[i] = ans

        # print(dp)
        return dp[0] - 1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        string = input()

        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends