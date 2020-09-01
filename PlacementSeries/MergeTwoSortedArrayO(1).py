# QUs: https: // www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/
# resource: https: // www.youtube.com/watch?v = hVl2b3bLzBw & list = PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2 & index = 4


def nextGap(gap):
    if(gap == 1):
        return 0

    return gap//2+1 if gap % 2 else gap//2


t = int(input())
for i in range(t):

    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    gap = n+m
    gap = nextGap(gap)

    while(gap):
        i = 0
        # first array
        while(i+gap < n):

            if(a[i] > a[i+gap]):
                a[i], a[i+gap] = a[i+gap], a[i]
            i += 1

        # both array

        while(i < n and i+gap < n+m):
            if(a[i] > b[i+gap-n]):
                a[i], b[i+gap-n] = b[i+gap-n], a[i]
            i += 1

        # second array
        while(i+gap < n+m):
            if(b[i-n] > b[i+gap-n]):
                b[i-n], b[i+gap-n] = b[i+gap-n], b[i-n]

            i += 1

        gap = nextGap(gap)

    # print both array
    for i in a:
        print(i, end=' ')

    for i in b:
        print(i, end=' ')

    print()
