# Qus:https://www.interviewbit.com/problems/spiral-order-matrix-i/

class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
            n = len(A)
            m = len(A[0])

            top,left,right,bottom = 0,0,m-1,n-1
            ans = []

            while(top<=bottom and left<=right):

                # move left to right from top

                for l in range(left,right+1):
                    ans.append(A[top][l])
                top += 1

                # move top to bottom from right

                for t in range(top,bottom+1):
                    ans.append(A[t][right])
                right -= 1

                # move right to left from bottom

                if(top<=bottom):

                    for r in range(right,left-1,-1):
                        ans.append(A[bottom][r])
                    
                    bottom -= 1

                # move from bottom to top 

                if(left<=right):

                    for b in range(bottom,top-1,-1):
                        ans.append(A[b][left])
                    
                    left += 1
            return ans







