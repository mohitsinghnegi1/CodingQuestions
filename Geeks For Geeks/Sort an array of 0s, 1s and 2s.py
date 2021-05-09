# Qus:https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

# Time complexity O(n)

# User function Template for python3

class Solution:
    def sort012(self, arr, n):
        # code here
        l, m, r = 0, 0, len(arr)-1

        while(m <= r):

            if(arr[m] == 0):
                arr[l], arr[m] = arr[m], arr[l]
                l += 1
                m += 1
            elif(arr[m] == 1):
                m += 1
            else:

                arr[r], arr[m] = arr[m], arr[r]
                r -= 1
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
