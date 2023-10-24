import sys


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        #         d = {}

        #         def get_min_coins(coins,amount):

        #             #  fewest number of coins
        #             if(amount==0):
        #                 return 0
        #             if(amount<0):
        #                 return sys.maxsize

        #             if(d.get(amount,None)!=None):
        #                 return d.get(amount)

        #             min_coins = sys.maxsize

        #             for i in range(len(coins)):

        #                 ncoins = 1 + get_min_coins(coins,amount - coins[i])
        #                 min_coins = min(ncoins,min_coins)

        #             d[amount] =  min_coins
        #             return d[amount]

        #         ans = get_min_coins(coins,amount)

        #         return ans if ans!=sys.maxsize else -1

        if (amount == 0):
            return 0

        if (len(coins) == 0):
            return -1

        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        min_coins = sys.maxsize

        for rem_amt in range(1, amount + 1):
            for i in range(len(coins)):

                if (rem_amt - coins[i] >= 0 and dp[rem_amt - coins[i]] != sys.maxsize):
                    dp[rem_amt] = min(1 + dp[rem_amt - coins[i]], dp[rem_amt])
                    # min_coins = min(dp[rem_amt],min_coins)

        return dp[-1] if dp[-1] != sys.maxsize else -1












