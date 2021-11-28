# Qus:https://www.geeksforgeeks.org/minimum-increment-operations-to-make-array-unique/

"""

Intution : if the count of some 


"""

def minIncrementForUnique(input2):
  counter = {} # store frequency
  
  for i in input2:
    counter[i] = counter.get(i,0)+1
  
  taken = []
  inc = 0
  for x in range(100000):
    if(counter.get(x,0)>=2):
      taken.extend([x]*(counter.get(x,0)-1))
    elif taken and counter.get(x,0)==0:
	   # we can use this value for top value which will always be less then x
      
      inc += x - taken.pop()
      
  
  
  return inc+sum(input2)

# Driver code
A = [1, 4, 5, 4, 5]
print(minIncrementForUnique(A))
