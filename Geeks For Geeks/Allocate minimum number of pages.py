# Qus:https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

"""
Timecomplexity o(nlogn)
"""


def isPossible(mid, arr, n, m):
    sum1 = 0
    count = 1
    for val in arr:
        if(val > mid):
            return False
        if(val + sum1 > mid):
            count += 1
            sum1 = val

            if(count > m):
                return False

        else:
            sum1 += val

    return True


class Solution:
    def findPages(self, arr, n, m):
        # n: no of book
        # m: no of students
        if(m > n):
            return -1

        l = 0
        r = sum(arr)+1

        while(l < r):

            mid = (l+r)//2

            if(isPossible(mid, arr, n, m)):
                r = mid
            else:
                l = mid+1

        return r

        # return: the expected answer if possible else return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        m = int(input())

        ob = Solution()

        print(ob.findPages(arr, n, m))
# } Driver Code Ends
