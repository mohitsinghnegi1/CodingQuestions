# Qus:https://www.geeksforgeeks.org/paths-requiring-minimum-number-of-jumps-to-reach-end-of-array/

# Python3 program to implement the
# above approach
def Solution(arr,i=0,step=0,path=''):
  
    path+=str(i)+'-> '
    if(i+arr[i]>=len(arr)):
      print(path)
      return


    for j in range(i+1,i+arr[i]):

      Solution(arr,j,step+1,path)
    
    
  
  
  
	
	

# Driver Code
if __name__ == "__main__":
	
	arr = [ 3, 3, 0, 2, 1,
			2, 4, 2, 0, 0 ]
	size = len(arr)
	ans = []
	Solution(arr)
    
    

# This code is contributed by akhilsaini
