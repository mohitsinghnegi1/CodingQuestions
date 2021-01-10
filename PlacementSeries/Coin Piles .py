# QUs:https://practice.geeksforgeeks.org/problems/coin-piles/0
# time complexity O(n**2)

import sys
t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if(len(a) == 0):
        print(0)
        continue

    """
        Remember we can also remove a complete pile
        it is not benificial to remove the greatest pile or even a pile greater
        then the min pile bec it will always be optimal to reducer the number
        of coins in the pile insted of removing complete pile (having a[i] coins)
        bec it will also add to the ans
        
        we can get optimal solution by removing the min pile though bec 
        consider a test case 1 99 99 99 so in this case removing fist pile will 
        give the best solution as we only need to remove 1 coin only insted of 
        bringing all other to 1 which is 98+98+98 
    
    """

    nCoinsToRemove = sys.maxsize  # let say we need to reduce this var
    a.sort()
    pf = 0
    for i in range(len(a)):
        bar = a[i]+k  # set max bar from cur element

        removeCoin = 0
        for j in range(i+1, len(a)):
            # since we have sorted the array to a[j] will always
            # be equal or greater the prev but the bar can be greater
            # so make sure you check below condition
            if(a[j] > bar):
                removeCoin += (a[j]-bar)

        nCoinsToRemove = min(nCoinsToRemove, pf+removeCoin)
        # this is the tile that we will remove entirely
        pf += a[i]  # prefix sum

    print(nCoinsToRemove)
