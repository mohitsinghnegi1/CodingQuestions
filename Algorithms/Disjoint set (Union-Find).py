# QUs:https://practice.geeksforgeeks.org/problems/disjoint-set-union-find/1#
# function should return parent of x

'''
    This union find algo is with rank , and path compression
    Note: 
    We are updating the root node par only  (If we update the current node parent only then it means we are just migrating one 
    node from one set to other) so by updating the root node means we are updating the whole set parent (ie doing actual union)

'''


'''
Input :
1
5 4
FIND 4 FIND 1 UNION 3 1 FIND 3

'''


def find(arr, x):
    # Code here

    par = x
    while(par != arr[par]):
        par = arr[par]
    return par

# function shouldn't return or print anything


def union(arr, x, z):
    # Code here

    parX = find(arr, x)
    parZ = find(arr, z)
    # we need to update the parent of root node , not the given node
    arr[parX] = parZ


T = int(input())
for _ in range(T):
    n, k = list(map(int, raw_input().strip().split()))
    arr = [0]+[x for x in range(1, n+1)]
    str1 = raw_input().strip().split()
    i = 0
    while i < len(str1):
        if str1[i] == 'FIND':
            print find(arr, int(str1[i+1])),
            i += 2
        elif str1[i] == 'UNION':
            union(arr, int(str1[i+1]), int(str1[i+2]))
            i += 3
