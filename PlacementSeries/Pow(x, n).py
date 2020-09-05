# Qus: https: // leetcode.com/problems/powx-n/
# runned on python 3

@lru_cache
def power(x, n):
    if(n <= 0):
        return 1

    halfPower = power(x, n//2)

    if(n % 2 == 1):

        return halfPower*halfPower*x
    return halfPower*halfPower


class Solution:

    def myPow(self, x: float, n: int) -> float:

        # handle for negative power only
        if(n < 0):
            return 1/power(x, -n)
        return power(x, n)


# second method0-------------------------------
# we can also use  (x*x)**(n/2)

@lru_cache
def power(x, n):
    if(n <= 0):
        return 1
    if(n % 2):
        return power(x*x, n//2)*x
    return power(x*x, n//2)


class Solution:

    def myPow(self, x: float, n: int) -> float:

        if(n < 0):
            return 1/power(x, -n)
        return power(x, n)
