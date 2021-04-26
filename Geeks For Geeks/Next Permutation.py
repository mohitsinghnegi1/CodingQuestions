# Qus:https://practice.geeksforgeeks.org/problems/next-permutation5226/1
# User function Template for python3
"""
    Intution :
    start from last index of arr find the pos where a[i]<a[i+1]

    swap elemnt present at pos and eleemnt just greater in right side of pos index 
    after that return a[:pos+1]+sorted(a[pos+1:])


""""


class Solution:
    def nextPermutation(self, N, arr):
        # code here
        pos = N-1

        for i in range(N-2, -1, -1):
            if(arr[i] < arr[i+1]):
                pos = i
                break
        # print(pos)

        if(pos == N-1):
            return arr[::-1]
        else:
            maxi = pos+1

            for j in range(pos+2, len(arr)):
                # print(arr[maxi],arr[j],arr[pos])
                if(arr[maxi] > arr[j] > arr[pos]):
                    maxi = j
                else:
                    break
                    # print(maxi)
            # print(pos,maxi)

            arr[pos], arr[maxi] = arr[maxi], arr[pos]
            # print(arr)
            return arr[:pos+1]+sorted(arr[pos+1:])


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i], end=" ")
        print()
# } Driver Code Ends
