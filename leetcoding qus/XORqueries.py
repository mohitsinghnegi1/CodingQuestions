
# Qus : https://leetcode.com/discuss/interview-question/794840/Google-or-Software-Engineer-Internship-2021-or-Online-test-questions-(OA)

# tag: google
#intution 
# instead of xor a[i] for 0<=i<len(a) every time we get a query of 1st type
# we can first calculate ans use xor^x[i] i for every type 1 query 
# becuse it will reduce O(n**2) complexity to O(n) time complexity for xoring
# O(nlogn ) for sorting


t=int(input())
for i in range(t):
    a=[0]#this array will contain inserted value x
    b=[0]#this array will contain xor value whenever we get query of type 1
    
    #this xor veriable will contian cur xor
    xor=0#initialize xor with 0 as number ^ 0 = number 
    
    q=int(input())
    
    #this count variable will hold number of queries of type 1
    #this variable we will use later after shorting to remove None values from a
    count=0
    
    for i in range(q):
        query,x=map(int,raw_input().split())
        #for query of type 0 
        # we will append x into a and None(any value as we we not use these val) in b

        if(query==0):
            a.append(x)
            b.append(None)
        else:
            #for type 1 query we will put x in b and None in a
            b.append(x)
            a.append(None)
            count+=1
    xor=0
    print b
    #triverse from back and ^ a[i] with latest xor value
    
    for i in range(len(a)-1,-1,-1):
        if(a[i]==None):
            xor=xor^b[i]
        else:
            a[i]=a[i]^xor
    
    a= sorted(a)
    print a
    #remove None after sorting
    #after sorting 
    print a[count:]
            