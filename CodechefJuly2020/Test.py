
def solve(infected,x):
    if(infected==x):
        return [1,x*2]
    if(infected<x):
        if(infected*2<x):
            return [1,x]
        else:
            return [1,infected*2]
    
    #if greater then x
    half=(infected/2+1 )if infected%2 else infected/2
    
    day=0
    while(x<half):
        x=x*2
        day+=1
    
    return [day+2,(infected)*2] if infected%2 else [day+2,(infected)*2]
    

t=int(input())
for i in range(t):
    n,x=map(int,raw_input().split())
    days=0
    infect=map(int,raw_input().split())

    infect.sort()

    for i in range(len(infect)):
        day,x=solve(infect[i],x)
        #print "day",day,"x",x
        days+=day
        
    
    
    print days
            
        
            
            
            
        
    