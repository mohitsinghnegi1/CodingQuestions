#Qus : https://www.hackerrank.com/contests/addskill-contest-13/challenges/knightl-on-chessboard/submissions
# """
# Sample Input 0

# 5
# Sample Output 0

# 4 4 2 8
# 4 2 4 4
# 2 4 -1 -1
# 8 4 -1 1
# """"
#sol 1:

import math
import os
import random
import re
import sys

global dp
dp={}


def bfs(x1,y1,a,b,n):
    
    if(dp.get((a,b),False)):
        return dp[(a,b)]
    
    #these are the list of eight moves that knight can make
    y_axis=[a,a,-a,-a,b,b,-b,-b]
    x_axis=[b,-b,b,-b,a,-a,a,-a]

    queue=[]
    queue.append((x1,y1,0))
    
    #visited array will keep track of all the moves that is already visited
    visited={}
    visited[(x1,y1)]=True
    
    while(queue):
        x1,y1,level=queue.pop(0)
        
        #assume this function will return all valid moves which are not yet visited
        
        for i in range(8):
            
            #next move
            x2=x1+x_axis[i]
            y2=y1+y_axis[i]
            level2=level+1
            
            
            #check if it is a valid move
            if(x2>=0 and x1<n and y2>=0 and y2<n and not visited.get((x2,y2),False)):
            
                #if knight reached to destination then return it level-->representing no of minimum moves
                if(x2==n-1 and y2==n-1):

                    #memorise a,b will give same result as b,a

                    dp[(b,a)]= dp[(a,b)]=level2

                    return dp[(b,a)]

                queue.append((x2,y2,level2))
                
                visited[(x2,y2)]=True
    
    #in case no possible path available    
    dp[(b,a)]=dp[(a,b)]=-1
    return dp[(a,b)]
            


# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
       
    for i in range(1,n):
        for j in range(1,n):
           
            ans=bfs(0,0,i,j,n)
            
            print ans,
        print 
        

n=int(input())
knightlOnAChessboard(n)


