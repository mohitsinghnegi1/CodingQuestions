# Qus:https://leetcode.com/problems/sum-of-square-numbers/solution/
# TLE

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        for i in range(0, c+1,):
            for j in range(i, c+1):
                # print i,j
                if(i**2+j**2 == c):
                    return True
        return False
# TLE


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0

        while(i*i <= c):
            j = 0
            while(j*j <= c):
                # print i,j
                if(i*i+j*j == c):
                    return True
                j += 1

            i += 1

        return False


# non TLE
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def isPerfectSquare(x):
            if(x < 0):
                return False
            if(x == 0):
                return True
            # print x
            b = math.sqrt(x)
            # print b
            return b == int(b)

        i = 0
        while(i*i <= c):
            x = c - i*i
            # print i,x

            if(isPerfectSquare(x)):
                return True
            i += 1

        return False


def binarySearch(x):

    l = 0
    r = x+1

    while(l < r):

        mid = (l+r)/2

        if(mid*mid == x):
            return True

        if(mid*mid > x):
            r = mid
        else:
            l = mid + 1

    return False

# non tle


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        i = 0
        while(i*i <= c):

            x = c - i * i

            if(binarySearch(x)):
                return True

            i += 1

        return False
