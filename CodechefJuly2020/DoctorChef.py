
import bisect

def solve(infected,x):
    
    if(x>=infected):
        return [1,infected*2]
    
    day=0
    half=infected/2+1 if infected%2 else infected/2
        
    while(x<half):
        x=2*x
        day+=1
    if(x==infected):
        return [1,infected*2]
    return [day+2 ,(infected-1)*2 if infected%2 else infected*2]
    

t=int(input())
for i in range(t):
    n,x=map(int,raw_input().split())
    days=0
    infect=map(int,raw_input().split())
    #we need to minimize the infection rate so for that we need to cure 
    
    
    #if all country population is less then current vaccine count then number of days = number of country 
    #think logical like first we will give vacine to max the second max then third mx and so on
    # if(max(infect)<=x):
    #     print len(infect)
    
    # else:
        #if there is  at least one country present whose population is greater then the number of vaccine 
        #then this block will gets executed
    temp=x
    
    infect.sort()
    
    initial=0
    for i in range(len(infect)):
        if(infect[i]<=x ):
            if(infect[i]*2>=x):
                days=i+1
                initial=i+1
                x=infect[i]*2
            else:
                days=i+1
                initial=i+1
        else:
            
            days=i
            initial=i
            break
       
    else:
        initial=len(infect)
        days=i
  
   
    
    
    
    for i in range(initial,len(infect)):
        day,x=solve(infect[i],x)
        #print "day",day,"x",x
        days+=day
        
    
    
    print days
            
        
            
            
            
        
    