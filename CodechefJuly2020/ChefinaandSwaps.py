from collections import OrderedDict

def isObtainable(a,b):
    xor=0
    for i,j in zip(a,b):
        xor^=i
        xor^=j
    if(xor==0):
        return True
    return False


def solve(a,b,min1):
    #
    d1=OrderedDict()
    d2=OrderedDict()
    for i,j in zip(a,b):
        d1[i]=d1.get(i,0)+1
        d2[j]=d2.get(j,0)+1
        
    # print d1,d2
    
    for i in d1.keys():
        if(i in d2):
            # print d1[i],d2[i]
            m=min(d1[i],d2[i])
            d1[i]=d1[i]-m
            d2[i]=d2[i]-m
            if(d1[i]==0):
                del d1[i]
            if(d2[i]==0):
                del d2[i]
                
    s1=[]      
    s2=[]
             
    for i in d1:
        d1[i]/=2
        s1+=[i]*d1[i]
    for j in d2:
        d2[j]/=2
        s2+=[j]*d2[j]
    
    # print s1,s2
    # print d1,d2
    
    ans=0
    for l,r in zip(s1,s2[::-1]):
        ans+=min(2*min1,min(l,r))
    return ans
        

t=int(input())
for _ in range(t):
    
    n=int(input())
    
    a=map(int,raw_input().split())
    b=map(int,raw_input().split())
    
    
    
    #check if ans is obtainable or not
    if(not isObtainable(a,b)):
        print -1
        continue
    
    a.sort()
    b.sort()
    
    ans=0
    if(a[0]==b[0]):
        ans=solve(a,b,a[0])
    elif(a[0]<b[0]):
        ans=solve(a,b,a[0])
    else:
        ans=solve(b,a,b[0])
    print ans
    
    # if(a[0]==b[0]):
        
        
    
    
    
    # else:
    #     #swap min with max in other array
        
    
    