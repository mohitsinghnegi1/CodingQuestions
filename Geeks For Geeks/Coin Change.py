# Qus:https://practice.geeksforgeeks.org/problems/coin-change2448/1
# tag - dp
# time complexity O(n*m)
# space complexity O(n)

# User function Template for python3

class Solution:
    def count(self, S, m, n):
        # code here

        a = [0]*(n+1)
        a[0] = 1  # use zero conins to produce 0 val

        for i in range(1, m+1):
            for j in range(1, n+1):
                if(j - S[i-1] >= 0):
                    # pick addition of both j-s[i] val and top val
                    a[j] = (a[j - S[i-1]] + a[j])

                    # pattern found - if you are reusing the same value
                    # multiple times then consider the current row else
                    # consider the row above it
            # print(a)
        # print(a)
        return a[-1]


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S, m, n))
# } Driver Code Ends
