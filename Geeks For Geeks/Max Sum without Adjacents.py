# Qus:https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1

# User function Template for python3
class Solution:

    def findMaxSum(self, arr, n):
        # code here
        if(len(arr) == 1):
            return arr[0]

        maxsum = [0]*len(arr)
        maxsum[0] = arr[0]
        maxsum[1] = max(arr[0], arr[1])

        if(len(arr) >= 3):
            maxsum[2] = max(arr[1], arr[0]+arr[2])

        for i in range(3, len(arr)):

            maxsum[i] = max(maxsum[i-1], arr[i]+max(maxsum[i-2], maxsum[i-3]))

# 		print(maxsum)
        return maxsum[-1]


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
