# https://www.interviewbit.com/problems/counting-subarrays/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        # always remember increase on r decrease on left
        l,r = 0,0
        sum = A[0]
        count = 0

        while(r<n):
            # print sum
            if(sum<B):
                r+=1

                if(l<=r):
                    count += r - l

                if(r<n):
                    sum+=A[r]


            else:
                sum-=A[l]
                l+=1




        return(count)





