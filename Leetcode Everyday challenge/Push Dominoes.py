# Qus:https://leetcode.com/problems/push-dominoes/
from collections import deque


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        """
        "0 1 2 3 4 5 6 7 8 9 10 11 12 13"
        ". L . R . . . L R .  .  L  .  ."
          -0.5  -1  0  1  -0.125  -0.25  -0.5  -1  1  -0.25   -0.5  -1   0   0
          -0.5  -1  0  1  0.5       0    -0.5  -1  1   0.5    -0.5  -1   0   0    
            L   L .  R  R . L L R R L L . .
       
        
        """
        out = []

        for i in range(len(dominoes)):
            if(dominoes[i] == '.'):
                out.append(0)
            elif(dominoes[i] == 'L'):
                out.append(-100)
            else:
                out.append(100)

        # print out
        for i in range(len(dominoes)-2, -1, -1):
            if(out[i+1] < 0 and out[i] == 0):
                out[i] = out[i+1]/2.0
        for i in range(1, len(dominoes)):
            if(out[i-1] > 0 and out[i] != 100 and out[i] != -100):
                if(out[i-1]/2.0+out[i] == 0):
                    out[i] = 0
                elif out[i-1]/2.0+out[i] > 0:
                    out[i] = out[i-1]/2.0

        # print out
        str1 = ""

        for i in range(len(out)):
            if(out[i] == 0):
                str1 += '.'
            elif(out[i] < 0):
                str1 += 'L'
            else:
                str1 += 'R'

        return str1


# slight modification instead of expensive divide operation i am uisng -+ operation


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        # calculate force

        n = len(dominoes)

        force = [0]*(n)
        f = 0
        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif(dominoes[i] == 'L'):
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f
        # print force
        f = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                f = n
            elif(dominoes[i] == 'R'):
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f
        # print force

        ans = ""
        for f in force:
            if(f == 0):
                ans += "."
            elif(f > 0):
                ans += "R"
            else:
                ans += "L"
        return ans
