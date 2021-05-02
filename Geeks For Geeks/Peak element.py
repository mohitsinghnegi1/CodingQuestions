# Qus:https://practice.geeksforgeeks.org/problems/peak-element/1

# your task is to complete this function
# function should return index to the any valid peak element
class Solution:
    def peakElement(self, arr, n):
        # Code here
        if(len(arr) == 1):
            return 0

        if(arr[0] >= arr[1]):
            return 0

        if(arr[-2] <= arr[-1]):
            # print("sd",len(arr)-1)
            return len(arr)-1

        l = 0
        r = len(arr)

        while(l < r):
            mid = (l+r)//2
            # print("mid",mid)
            if((mid-1 < 0 or (arr[mid-1] <= arr[mid])) and (mid+1 >= len(arr) or (arr[mid] >= arr[mid+1]))):
                # print('1')
                return mid
            elif(mid+1 < len(arr) and arr[mid] < arr[mid+1]):
                # print('2',mid+1)
                l = mid + 1
            else:
                r = mid
                # print('3',r)
        return l


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] >= arr[index+1]:
                flag = True
            elif index == n-1 and arr[index] >= arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
