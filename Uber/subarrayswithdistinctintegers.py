from collections import defaultdict
# https://www.interviewbit.com/problems/subarrays-with-distinct-integers/
# rat loo isko , two pointer when we need to find what is the possible subset having at max 4 unique or sum less then someting
def countSubarrayWithMaxNunique(n,A):

    length = len(A)

    l,r = 0,0

    d = defaultdict(list)
    d[A[0]].append(0)
    count = 0

    while(l < length and r < length):

        uniques = len(d)

        if(uniques<=n):
            r+=1

            if(l<=r):
                count += (r - l)

            if(r<length):
                d[A[r]].append(r)
                # print "append",A[r]

        else:
            # pop
            # print "no"
            d[A[l]].pop()

            if(len(d[A[l]])==0):
                del d[A[l]]

            l+=1
    # print d
    print count
    return count

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):


        return countSubarrayWithMaxNunique(B,A)-countSubarrayWithMaxNunique(B-1,A)



