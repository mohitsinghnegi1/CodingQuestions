# Qus : https://www.hackerrank.com/contests/addskill-contest-13/challenges/largest-rectangle
# QUs : https://leetcode.com/problems/largest-rectangle-in-histogram/
# SOL:


import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack=[]
    max_area=0
    i=0
    while(i<len(h)):
        if(stack==[] or h[stack[-1]]<=h[i]):
            stack.append(i)
            i+=1
        else:
            top=stack.pop()
            if(stack==[]):
                max_area=max(h[top]*i,max_area)
                
            else:
                max_area=max(h[top]*(i-1-stack[-1]),max_area)
    
    while(stack!=[]):
        top=stack.pop()
        if(stack==[]):
            max_area=max(h[top]*i,max_area)
                
        else:
            max_area=max(h[top]*(i-1-stack[-1]),max_area)     
    return max_area
        
        
        



n = int(raw_input())

h = map(int, raw_input().rstrip().split())

result = largestRectangle(h)

return result
