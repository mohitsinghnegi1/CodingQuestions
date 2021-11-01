# Qus:https://www.interviewbit.com/problems/gas-station/
# n**2 sol
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, A, B):

            for i in range(len(A)):
                
                j = (i+1)%len(A)
                fuel = A[i] - B[i]

                while(j!=i and fuel>=0 ):
                    fuel += (A[j] - B[j])
                    j= (j+1)%len(A)
                    
                
                if(i==j and fuel>=0):
                    return i
            return -1


# efficient O(N) solution

class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, A, B):

            if(sum(A)<sum(B)):
                return -1

            fuel = 0
            ans = 0
            for i in range(len(A)):
                fuel += (A[i] - B[i])

                if(fuel<0):
                    # this could not be the ans

                    ans = i+1
                    fuel = 0
            return ans


