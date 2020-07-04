def sumofdigit(n):
    sum1=0
    while(n):
        sum1+=n%10
        n=n/10
    return sum1
    

t=int(input())
for i in range(t):
    n=int(input())
    chef,morty=0,0
    for i in range(n):
        ai,bi=map(int,raw_input().split())
        sa=sumofdigit(ai)
        sb=sumofdigit(bi)
        if(sa==sb):
            chef+=1
            morty+=1
        elif(sa<sb):
            morty+=1
        else:
            chef+=1
    if(chef>morty):
        print 0,chef
    elif(chef<morty):
        print 1,morty
    else:
        print 2,chef
        