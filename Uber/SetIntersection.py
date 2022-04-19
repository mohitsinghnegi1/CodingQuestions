# https://www.interviewbit.com/problems/set-intersection/
#  Time complexity O(n)


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def setIntersection(self, A):


        A = sorted(A,key = lambda x:(x[1],x[0]))
        # print(A)

        a,b = A[0][-1]-1,A[0][-1]
        count = 2

        for i in range(1,len(A)):
            # print(a,b)

            l,r = A[i]

            if(b<l):
                # skip
                a,b = r-1,r
                count +=2

            elif(a<l):
                #skip
                a,b = b,r
                count += 1
            elif(b==l): #[1,1]
                print(a,b,l)
                a,b = b,r
                count +=1

        return count





