# Qus:https://www.hackerrank.com/contests/addskill-contest-13/challenges/cavity-map


import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    ans=[]
    for i in range(len(grid)):
        r=""
        for j in range(len(grid)):
            if(i!=0 and i!=len(grid)-1 and j!=0 and j!=len(grid[i])-1 and grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i][j+1]):
                r+='X'
            else:
                r+=grid[i][j]
        ans.append(r)
    return ans
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grid = []

    for _ in xrange(n):
        grid_item = raw_input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
