# User function Template for python3
import sys


class Solution:
    def matrixMultiplication(self, N, arr):
        # code here

        """
        Imagine 1 metrics
        Imagine 2 metrics getting multiply (AB)(A). (2*3|*3*6)*|(6*5) =
            (AB)(A)
                -> 2*6*5 + 36 = 60+36 = 96
                    -> (AB) = 2*3*6 + 0 = 36
                        -> (A) = 0
                        -> (B) = 0
                    -> (A) = 0
            (A)(BA)
                -> 0 + 90
                   -> (BA) = 3*6*5 + 0 = 90
                        -> B = 0
                        -> A = 0

            min() = 90



        """

        # d = {}
        # def mcm(i,j):

        #     # means there is only one metrics so , number of operations required = 0
        #     if(i==j):
        #         return 0

        #     if(d.get((i,j),None)!=None):
        #         return d.get((i,j),None)

        #     # k is a point of bracket

        #     # j will be excluded as arr[j-1]*arr[j]

        #     min_operations = sys.maxsize

        #     for k in range(i,j):
        #         operations = mcm(i,k) + arr[i-1]*arr[k]*arr[j] + mcm(k+1,j)
        #         min_operations = min(min_operations,operations)

        #     d[(i,j)] = min_operations
        #     return d[(i,j)]

        # # n is excluded
        # return mcm(1,N-1)

        """
        convert into dp approach


        form a square , see what is calaculated first, it appears , bottom right corner


        """

        dp = [[0] * N for _ in range(N)]

        for i in range(N - 1, 0, -1):
            for j in range(i + 1, N):

                min_operations = sys.maxsize
                for k in range(i, j):
                    operations = dp[i][k] + arr[i - 1] * arr[k] * arr[j] + dp[k + 1][j]
                    min_operations = min(min_operations, operations)

                dp[i][j] = min_operations

        return dp[1][N - 1]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends