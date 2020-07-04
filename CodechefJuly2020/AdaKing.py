t=int(input())
for _ in range(t):
    k=int(input())
    x=0
    
    for i in range(8):
        o=''
        
        for j in range(8):
            if(x<k):
                o+='.'
                
            else:
                o+='X'
            x+=1
            
        if(i==0):
            print 'O'+o[1:]
        else:
            print o

                
            