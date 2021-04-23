# Qus:https://www.geeksforgeeks.org/value-to-be-subtracted-from-array-elements-to-make-sum-of-all-elements-equals-k/
# code
def getCollected(height, cut):
    collected = 0
    for i in range(len(height)-1, -1, -1):
        if(height[i] - cut > 0):
            collected += (height[i] - cut)
        else:
            break
    return collected


def collectKWood(height, n, k):

    height.sort()
    if(len(height) == 0):
        if(k == 0):
            return 0
        else:
            return -1

    l = 0
    r = height[-1]+1

    while(l < r):
        mid = (l+r)//2
        collected = getCollected(height, mid)
        # print(collected)
        if(collected == k):

            return mid
        elif(collected > k):
            l = mid + 1
        else:
            r = mid
    else:
        return -1


# Driver code
height = [1, 2, 1, 2]
n = len(height)
k = 2

print(collectKWood(height, n, k))
