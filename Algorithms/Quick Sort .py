# Qus:https://practice.geeksforgeeks.org/problems/quick-sort/1

# User function Template for python3

class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if(low >= high):
            return

        pi = self.partition(arr, low, high)
        self.quickSort(arr, low, pi-1)
        self.quickSort(arr, pi+1, high)

    def partition(self, arr, low, high):

        # code here
        # this partition function will put the arr[high] in its right pos
        pi = low  # all the element that are greater then this eleemnt should be
        # on the right side of the pi
        l, r = low+1, high     # 2,0
        while(l <= r):

            # move l until you find a eleemtn greater then or equal to the pivot
            while(l <= r and arr[l] < arr[pi]):
                l += 1

            # move r to left until you find eleemnt less then pivot
            while(l <= r and arr[r] >= arr[pi]):
                r -= 1

            # swap the l, and r max and min
            if(l <= r):
                arr[l], arr[r] = arr[r], arr[l]
                l += 1  # increment l
                r -= 1  # decreemtn r Note this
            # print(l,r)

        arr[pi], arr[r] = arr[r], arr[pi]  # at the end swap pi with r
        return r


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        Solution().quickSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends
