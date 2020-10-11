# QUs: https://www.geeksforgeeks.org/count-number-subarrays-given-xor/


# time complexity O(n^2)
a=map(int,raw_input().split())
m=int(input())

count=0

for i in range(len(a)):
    xor=0
    for j in range(i,len(a)):
        xor^=a[j]
        if(xor==m):
            count+=1

print count


# efficient solution O(n) solution space complexity O(n) for hashmap
from collections import defaultdict
a=map(int,raw_input().split())
givenXor=int(input())

#concept used 
# let say xor of 0,..,i,i+1,..,j ==xor
# let say xor of 0,..,i = a
# let say xor of i+1,..,j = b

# so per the qus we need to find number of subarray with the given sum
# see the below test case for better understanding
#test case 0....0,6 so total xor possible subarray  will be 3  ie 0(....0,6),                 #0....0(6),0....0,6

# so we will be storing xor till i in hasmap with the count of xor as value 
# so every time we check if xor^givenXor in hashmap if yes then we will increament 
# the ans by hashmap=[xor^m]
# if cur xor ie 0..j equal to giveen xor then also we need to increase the ans by 1


ans=0
xor=0
hashmap=defaultdict(int)

for i in range(len(a)):
    #if prefix xor sum is equal to given xor then increament ans by 1
    # means xor from 0...i is equal to given xor then increament ans by 1
    xor=xor^a[i]
    if(xor==givenXor):
        ans+=1
    
    #there is possibility that there might be some other subarray which
    #ends at i having xor as givenXOr
    #test case 0....0,6 so total xor possible subarray  will be 3  ie 0(....0,6),                 #0....0(6),0....0,6
    
    ans+=hashmap.get(xor^givenXor,0)
    
    #update cur val of xor(0..i) into hasmap
    hashmap[xor]+=1
    
print ans

