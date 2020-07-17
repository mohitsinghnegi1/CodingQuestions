#given array whose prefix sum we want
#resource L https://www.hackerearth.com/practice/notes/binary-indexed-tree-or-fenwick-tree/#c217533
a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n=len(a)
#now we want to build binary index tree in following fashion
#lets dive into how we can build a binary indexed treee

# BIT[1]=a[1]
# BIT[2]=a[1]+a[2]
# BIT[3]=a[3]
# BIT[4]=a[1]+a[2]+a[3]+a[4]
# BIT[5]=a[5]
# BIT[6]=a[5]+a[6]
# BIT[7]=a[7]
# BIT[8]=a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]
# BIT[9]=a[9]
# BIT[10]=a[9]+a[10]
# BIT[11]=a[11]
# BIT[12]=a[9]+a[10]+a[11]+a[12]
# BIT[13]=a[13]
# BIT[14]=a[13]+a[14]
# BIT[15]=a[15]
# BIT[16]=a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]+a[13]+a[14]+a[15]+a[16]

#final BIT array after construcntion : [0, 1, 3, 3, 10, 5, 11, 7, 36, 9, 19, 11, 42, 13, 27, 15, 136]

#we get the len of range by using isolating last set bit using formula X&(-X)
#range will be start from x to i where i-x+1 is equal to length of range  (here x = X&(-X))
#BIT[i] will strore sum of all element in a in that calculated range

# NOTICE:

#                {           a[x],                  if x is odd
# BIT[x] =                   a[1] + ... + a[x],     if x is power of 2
#                }

# Sum of first 12 numbers in array = BIT[12] + BIT[8] = (a[12] +  + a[9]) + (a[8] +   + a[1])

# Similarly, sum of first 6 elements = BIT[6] + BIT[4] = (a[6] + a[5]) + (a[4] +   + a[1])

# Sum of first 8 elements = BIT[8] = a[8] +    + a[1]


#We construct the BIT using update function

BIT=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def update(BIT,n,diff,x):
    #a[13] is included in 3 rnages. 13 14 16
    #we need to update diff in all ranges
    #since this is prefix sum so need to add diff only (in case of product prefix we need to divide by old and multiply by new number need to add)
    
    while(x<n):
        assert x<len(BIT) and x>0, "Oh no!  assertion failed!"
        #add diff in all ranges
        print x,len(BIT)
        BIT[x]+=diff  #diff mean = new Val- old elemnt at index x
        
        #increament by steps equal to set bit 
        #for ex for 13 ie 1101 -> we will add one to x 
        #for 14 ie 1110 we add 2 since last set bit of 14 is 10 in binary=2 in decimal
        #for 16 we comes to end upto n we need to do this process
        x+=x&(-x)

for i in range(1,len(a)):
    update(BIT,n,a[i],i)
    #i am updating a[i] in BIT  at index i
    #since initially BIT[i] =0 so diff is the number itself
    
print BIT

# If we look at the for loop in update() operation, we can see that the loop runs at most the number of bits
#  in index x which is restricted to be less or equal to n (the size of the given array), so we can say that 
# the update operation takes at most O(log2(n)) time.

#now question arises that How to query such structure for prefix sums Let s look at the query operation.

def query(x,BIT):
    # x=index upto which we need sum of the elements
    sum1=0
    while(x>0):
        sum1+=BIT[x]
        x-=x&(-x)
    return sum1


#How this query function is working
# lets take an example of query(14,BIT)

# initially sum1=0 

# In then first loop we have added BIT[14] to sum1 
# ie sum1=BIT[14]=a[14]+a[13]   
# as we know BIT[14] contain sum of range 13 to 14 why? bec each element of BIT at index i contains sum 
# of elemnt from range i-(last set bit ie in this(14) case 10=2)

# In second loop x becomes 12 ie X-=X&(-X)
# sum1=BIT[14]+BIT[12]  ie a[14]+a[13] +a[12]+a[11]+a[10]+a[9]

# In 3rd loop x becomes 8 
# sum1=BIT[14]+BIT[12]+BIT[8] ie BIT[8]=a[8]+a[7]+a[6]+a[5]+a[4]+a[3]+a[2]+a[1]

# hence at the end sum1 will contain a[14]+a[13]+a[12]+a[11]+a[10]+a[9]+a[8]+a[7]+a[6]+a[5]+a[4]+a[3]+a[2]+a[1]


# Note these no of loops indicates no of ranges required to get the sum from 0 to x


#query sum of first 8 element
print query(8,BIT)
print query(1,BIT)
print query(3,BIT)
print query(4,BIT)
print query(4,BIT)-query(2,BIT)  #to get sum of 2elemnt present in 3rd and 4th  array index

update(BIT,n,1,1)
print query(16,BIT)
print BIT