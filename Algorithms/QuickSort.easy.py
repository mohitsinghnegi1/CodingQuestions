#User function Template for python3
# https://practice.geeksforgeeks.org/problems/quick-sort/1

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here

        if(low>=high):return

        pi =  self.partition(arr,low,high)

        self.quickSort(arr,low,pi-1)
        self.quickSort(arr,pi+1,high)




    def partition(self,arr,low,high):
        # code here

        pi = high
        l = low
        r = high - 1



        while(l<=r):
            # imaging all element before pi defined is less then the pi , l will reach up to pi index
            # and swap will pi at the end

            while(l<=r and arr[l]<=arr[pi]):
                l += 1

            # imaging all element before pi are greater then arr[pi] in that case r will go upto -1 index
            # from both case we conclude that we need to swap with l with pi

            while(l<=r and arr[r]>arr[pi]):
                r -= 1


            if(l<=r):
                arr[l],arr[r] = arr[r],arr[l]

        arr[l],arr[pi] = arr[pi],arr[l]

        return l



#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends