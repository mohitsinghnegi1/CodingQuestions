# Qus:https://www.geeksforgeeks.org/counting-inversions/

# --brute force using intsertion sort

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    icount = 0
    for i in range(n-1):
        for j in range(n-1):
            if(a[j] > a[j+1]):
                icount += 1
                a[j+1], a[j] = a[j], a[j+1]
    print(icount)
