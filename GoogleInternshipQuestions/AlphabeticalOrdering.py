#Albhabet Ordering

"""

minimum number of monotonic sequences (increasing or decreasing)
test cases:
abcdcdefa
3
abcdcba
2

"""

s=raw_input()
if(len(s)<=1):
    print 1

#we are building new array from string s such that no two adjucent element are equal
s1=[]
for i in s:
    if(s1!=[] and s1[-1]==i):
        pass
    s1.append(i)
    

#flag shows weather cur sequence is increasing or decreasing
flag=1 if s[0]<s[1] else -1
#count will store minimum number of monotonic substring (increasing or decreasing)
count=1

i=2

while(i<len(s)):
    
    if(s1[i-1]<s1[i] and flag!=1):
        count+=1
        #once we find a breaking point 
        #the sequence can either go up or down
        #based on that we need to set the flag 
        if(i+1<len(s) and s1[i]>s[i+1]):
            flag=-1
        else:
            flag=1
    elif(s1[i-1]>s1[i] and flag!=-1):
        count+=1
        if(i+1<len(s) and s1[i]>s[i+1]):
            flag=-1
        else:
            flag=1
    i+=1
print count
        
    
