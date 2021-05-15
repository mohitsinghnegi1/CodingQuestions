Qus: https: // practice.geeksforgeeks.org/problems/faithful-numbers0014/1

# User function Template for python3
sevenPower = []
for i in range(18):
    sevenPower.append(7**i)


class Solution:
    def nthFaithfulNum(self, N):
        # code here
        pow1 = 0
        ans = 0
        j = 0
        while(j <= 17):
            if(N & 1 << j):
                ans += sevenPower[pow1]
            pow1 += 1
            j += 1
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.nthFaithfulNum(N))
# } Driver Code Ends
