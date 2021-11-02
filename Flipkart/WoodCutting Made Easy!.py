# Qus:https://www.interviewbit.com/problems/woodcutting-made-easy/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        r = max(A)+1
        l = 0
        ans = 0 # we need to maximize the ans

        def isPossibleAns(mid):

            cut = 0

            for i in range(len(A)):
                if(A[i]>mid):
                    cut += (A[i]-mid)
            return (cut>=B)
        while(l<r):
            mid = (l+r)//2

            if(isPossibleAns(mid)):
                ans = max(ans,mid)
                l = mid+1
            else:
                r = mid
        return ans

