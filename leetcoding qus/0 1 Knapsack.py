def maxProfit(values, weights, n, w):

    # Write your code here

    # fraction: use greedy
    # 0/1 : use dp

    # dp= {}

    # def getMaxProfit(i,remW):
    #     # i is the item
    #     # remW is remaining weight
    #     # base condition
    #     if(i>=n or remW<=0):
    #         return 0

    #     if(dp.get((i,remW),None)!=None):
    #         return dp[(i,remW)]

    #     # should i pick or not?
    #     pick = 0
    #     if(weights[i]<=remW):
    #         pick = values[i]+getMaxProfit(i+1,remW-weights[i])
    #     dontPick = getMaxProfit(i+1,remW)

    #     # return max benifit choice
    #     dp[(i,remW)] =  max(pick,dontPick)
    #     return dp[(i,remW)]

    # return getMaxProfit(0,w)

    # recurrence relation
    """

    Change required to convert memo to dp
    1. Find the order of i and j based on the recursion flow (understance which pos is computed first, create a square corrdinate method to understand the order)
    2. change the function call with dp[i][j]
    3. answer will be stored in initial function call used in recurence solve


    dp[i][remW] represents , max profilt : given we have i items and remW weight


    dp[i+1][remW-weights[i]]
    dp[i+1][remW]

    # i will start from n-1
    # remW will start from 0 to w
    # answer will be stored at dp[0][w]

    """

    # max_profit = 0
    # dp = [[0]*(w+1) for i in range(n+1)]

    # for i in range(n-1,-1,-1):
    #     for remW in range(1,w+1):

    #         # should i pick or not?
    #         pick = 0
    #         if(weights[i]<=remW):
    #             pick = values[i]+dp[i+1][remW-weights[i]]
    #         dontPick = dp[i+1][remW]

    #         # return max benifit choice
    #         dp[i][remW] =  max(pick,dontPick)
    #         # max_profit = max(max_profit,dp[i][remW])
    # # print(dp)
    # return dp[0][w]


    """
    In space optimized approach what i did?

    1. convert 2d dp into single dp after rightly understanding the iteration flow and the previous dp 
    value required . 
    2. You might need to change the order of i or j 
    3. instead of using dp[i][j] we just need to use dp[j]
    
    
    
    
    
    """

    max_profit = 0
    dp = [0]*(w+1)

    for i in range(n-1,-1,-1):
        for remW in range(w,0,-1):

            # should i pick or not?
            pick = 0
            if(weights[i]<=remW):
                pick = values[i]+dp[remW-weights[i]]
            dontPick = dp[remW]

            # return max benifit choice
            dp[remW] =  max(pick,dontPick)
            # max_profit = max(max_profit,dp[i][remW])
    # print(dp)
    return dp[w]














