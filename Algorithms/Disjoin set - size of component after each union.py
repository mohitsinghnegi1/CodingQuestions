# QUs:https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/tutorial/

# Write your code here


def printSize(par):
    out = []
    for i in par:
        if(i < 0):
            out.append(abs(i))
    out.sort()

    print " ".join(map(str, out))


def find(u):

    while(par[u] >= 0):
        u = par[u]
    return u


n, m = list(map(int, raw_input().split()))

par = [-1]*n  # -1. - denotes the root set root value and 1 denotes magnitude of set


for i in range(m):
    u, v = map(int, raw_input().split())

    paruIdx = find(u-1)  # RETURN INDEX
    parvIdx = find(v-1)  # RETURN INDEX

    if(paruIdx == parvIdx):
        continue

    if(abs(par[paruIdx]) > abs(par[parvIdx])):
        # also increse rank of u

        par[paruIdx] += par[parvIdx]

        par[parvIdx] = paruIdx
        par[v-1] = paruIdx
    else:
        # increase rank of v

        par[parvIdx] += par[paruIdx]

        par[paruIdx] = parvIdx

        par[u-1] = parvIdx

    # merge happend , print the size of each components
    printSize(par)
