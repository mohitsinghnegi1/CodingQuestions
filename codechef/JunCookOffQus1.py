n, q = map(str, raw_input().split())
a = map(str, raw_input().split())
p = []


def product(q):
    p = 1
    for i in range(len(a)):
        p *= (q - a[i])

    return p


for i in range(q):
    q = int(input())
    ans = product(q)

    if(ans == 0):
        print 0
    elif(ans < 0):
        print "NEGATIVE"
    else:
        print "POSITIVE"
