# Qus:https://practice.geeksforgeeks.org/problems/finger-game1755/1
# User function Template for python3
class Solution:
    def fingerCount(self, N):
        # code here

        d = {i: i for i in range(1, 5+1)}
        d[0] = 2
        d[6] = 4
        d[7] = 3

        return d[N % 8]


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        answer = ob.fingerCount(n)

        print(answer)


# } Driver Code Ends
