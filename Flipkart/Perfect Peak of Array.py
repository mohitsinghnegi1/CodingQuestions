# Qus:https://www.interviewbit.com/problems/perfect-peak-of-array/
"""
prefixMax 
siffix min is required in this qus

"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):

        if(len(A)<=2):
            return 0

        prefixMax = [A[0]]
        for i in range(1,len(A)):
            prefixMax.append(max(prefixMax[-1],A[i]))
        
        suffixMin = [0]*len(A)
        suffixMin[-1]= A[-1]

        for i in range(len(A)-2,-1,-1):
            suffixMin[i] = min(suffixMin[i+1],A[i])
        # print(prefixMax,suffixMin)

        for i in range(1,len(A)-1):
            if(prefixMax[i-1]<A[i] and A[i]<suffixMin[i+1]):
                # print(A[i],i,prefixMax,suffixMin)
                return 1
        return 0





