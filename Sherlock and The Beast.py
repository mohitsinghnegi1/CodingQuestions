#Qus:https://www.hackerrank.com/contests/addskill-contest-16/challenges


#!/bin/python

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    
    #5*tc indicate a number that is divisible by 5 (in our cade this whole term indicte count of 3 we can add to form a decent number)
    #(n-5*tc)%3 indicate a number which is divisible by 3 ,here n-5*tc indicate count of 5 . 
    #for our case we want n-5*tc should also be divisible by 3
    tc=0
    while(5*tc<=n):
        
        if(n-5*tc)%3==0:
            break
        tc+=1
    
    if(5*tc>n):
        print "-1"
    else:
        print '5'*(n-5*tc)+'3'*(5*tc)
        
    
if __name__ == '__main__':
    t = int(raw_input().strip())

    for t_itr in xrange(t):
        n = int(raw_input().strip())

        decentNumber(n)
