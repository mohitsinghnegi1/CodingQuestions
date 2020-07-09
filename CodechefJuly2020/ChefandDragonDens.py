n,q=map(int,raw_input().split())
h=map(int,raw_input().split())
a=map(int,raw_input().split())

def solveQuery(a,h,s,d):
    if(s==d):
        return a[s]
   
    if(h[s]<=h[d]):
        return -1
    #left to right
    
    if(d<s):
        sum1=a[d]
        minH=h[d]
        maxH=h[s]
        #print sum1,minH,maxH
        for i in range(d+1,s+1):
            if(h[i]>minH):
                if(h[i]>=maxH and i!=s):
                    #print "height",h[i],maxH
                    return -1               
                minH=h[i]
                sum1+=a[i]
        return sum1
        
        
    #right to left
    else:
        
        sum1=a[d]
        minH=h[d]
        maxH=h[s]
        for i in range(d-1,s-1,-1):
            if(h[i]>minH):
                if(h[i]>=maxH and i!=s):
                    return -1               
                minH=h[i]
                sum1+=a[i]
        return sum1
                

for i in range(q):
    x,s,d=map(int,raw_input().split())
    if(x==2):
                
        #if source is greater then destination then only move to next
        #min and max possible height
        print solveQuery(a,h,s-1,d-1)
    else:
        a[s-1]=d

        
    