t=int(input())
for _ in xrange(t):
    n=int(input())
    a=map(int,raw_input().split())
    diff=0
    for i in range(1,n):
        diff+=max(a[i],a[i-1])-min(a[i],a[i-1])-1
    print diff
        
        
        