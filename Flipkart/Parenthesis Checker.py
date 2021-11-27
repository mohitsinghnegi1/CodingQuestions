
#User function Template for python3




class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        stack = []
        
        close = [')','}',']']
        
        opositeBrac = {')':'(',']':'[','}':'{'}
        
        
        for i in x:
            
            if(stack==[] and i in close):
                return False
            if(stack==[]):
                stack.append(i)
            elif(i not in close):
                stack.append(i)
            
            elif(stack[-1]==opositeBrac[i]):
                stack.pop()
            else:
                return False
        if(stack!=[]):
            return False
        return True
            
            
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends