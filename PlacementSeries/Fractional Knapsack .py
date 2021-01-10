# QUs:https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1#
# User function Template for python3
import sys
import io
import atexit


def fractionalknapsack(W, Items, n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code

    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    n = len(Items)
    # sort items based on value by waight ration
    # as we want max value using least waight
    Items.sort(reverse=True, key=lambda x: (x.value+0.0)/(x.weight+0.0))
    # print(Items)
    # for item in Items:
    #     print(item.value,item.weight)

    i = 0
    profit = 0  # this will store profit that we can make by including
    # the items in dec order of their value/weight ratio
    # either we are left with no item or we are done with max weight
    # we will break the loop
    while(i < n and W != 0):

        # if we have sufficient weight to hold complete item
        # then we simply reduce the W by current item weight
        if(W > Items[i].weight):
            W -= Items[i].weight
            profit += Items[i].value
            i += 1
        else:

            # fraction of this item we can take
            remainingWeight = (W)  # we will take the fraction of this item

            # the value of profit that we can get from cur item
            # is the value by weight ratio * remaing weight
            value = ((Items[i].value+0.0) /
                     (Items[i].weight+0.0))*remainingWeight
            # print("rem",remainingWeight,value,W)
            profit += value
            W = 0
            i += 1

    return profit


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, W = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        Items = [Item(0, 0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]

        print("%.2f" % fractionalknapsack(W, Items, n))

# } Driver Code Ends
