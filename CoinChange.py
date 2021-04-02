# QUs:https://leetcode.com/problems/coin-change/

# brute force approach
import sys


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        coins.sort()

        def minCoins(amount, i, numCoins):

            if(i >= len(coins) or amount < 0):
                return sys.maxsize
            if(amount == 0):
                return numCoins

            # return min out of all possible ways
            # take dont take i

            return min(minCoins(amount-coins[i], i, numCoins+1),
                       minCoins(amount-coins[i], i+1, numCoins+1),
                       minCoins(amount, i+1, numCoins))

        minCoin = minCoins(amount, 0, 0)
        return minCoin if minCoin != sys.maxsize else -1

# using 2d dp


def getDpMatrix(coins, amount):
    dp = []

    for i in range(len(coins)):
        v = []
        for j in range(amount+1):
            if(j == 0):
                v.append(0)
            else:
                v.append(sys.maxsize)
        dp.append(v)
    return dp


def getMinCoins(dp, coins, amount):

    for coinIndex in range(len(coins)):
        for target in range(1, amount+1):

            # intution dp[coinIndex][target] = dp[coinIndex][target - coins[coinIndex]]+1
            # also possible to find target using less number of coins

            if(target - coins[coinIndex] >= 0 and dp[coinIndex][target - coins[coinIndex]] != sys.maxsize):
                dp[coinIndex][target] = dp[coinIndex][target - coins[coinIndex]]+1

            if(coinIndex-1 >= 0):
                dp[coinIndex][target] = min(
                    dp[coinIndex][target], dp[coinIndex-1][target])

    # print dp
    return dp[-1][-1] if dp[-1][-1] != sys.maxsize else -1


class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = getDpMatrix(coins, amount)

        minCoins = getMinCoins(dp, coins, amount)

        return minCoins


# remember dont think that 5 5 1 1 1 1  will not give optimal result
# 5 5 4 is more optimal to choose

# efficient solution


class Solution3(object):
    def __init__(self):
        self.mincoin = sys.maxsize

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if(amount == 0):
            return 0
        if(len(coins) == 0):
            return -1

        # each element at index i of this array represent
        # what is the min number of coins required to get a value i
        minCoins = [sys.maxsize]*(amount+1)
        # to get a value 0 we need min 0 number of coins
        minCoins[0] = 0
        coins.sort()

        for i in range(1, amount+1):
            # try out each coin and substract from current i and update min coin at current position
            for j in range(len(coins)):
                if(i-coins[j] < 0):
                    break
                if(minCoins[i-coins[j]]+1 < minCoins[i]):
                    minCoins[i] = minCoins[i-coins[j]]+1

        # incase current position is sys.maxsize then it means not posssible to make that sum
        return minCoins[-1] if minCoins[-1] != sys.maxsize else -1
