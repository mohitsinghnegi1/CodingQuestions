t=int(input())
for _ in range(t):
    n=int(input())
    xor,yor=0,0
    for i in range(4*n-1):
        x,y=map(int,raw_input().split())
        xor^=x
        yor^=y
    print xor,yor
        