import math 
n,q=map(int,raw_input().split())
h=map(int,raw_input().split())
a=map(int,raw_input().split())
x = (int)(math.ceil(math.log(n,2)));  
  
# Maximum size of segment tree  
max_size = 2 * (int)(2**x) - 1;  
   
st = [-1] * (max_size);  

st2=[-1] * (max_size);  

def constructSegmentTree(h,a,st,low,high,pos):
    
    if(pos>=len(st)):
        return
    #print "["+str(low)+" "+str(high)+"]"
    if(low==high):
        assert pos<len(st),""+str(pos)+" "+str(len(st))
        assert low<len(a)
        st[pos]=a[low]
        return
    mid=(low+high)/2
    constructSegmentTree(h,a,st,low,mid,pos*2+1)
    constructSegmentTree(h,a,st,mid+1,high,pos*2+2)
    
    if(h[high]<=h[low]):
        st[pos]=-1
        return 
    #left to right
    sum1=a[low]
    minH=h[low]
    maxH=h[high]
    #print sum1,minH,maxH
    for i in range(low,high+1):
        if(h[i]>minH):
            if(h[i]>=maxH and i!=high):
                #print "height",h[i],maxH
                st[pos]=-1       
                return       
            minH=h[i]
            sum1+=a[i]
    st[pos]=sum1


    
    




constructSegmentTree(h,a,st,0,n-1,0)

constructSegmentTree(h[::-1],a[::-1],st2,0,n-1,0)



#construction of Segment tree is done
# print st
# print st2

def getMid(s, e) : 
    return s + (e - s) // 2; 

def RMQUtil( st, ss, se, qs, qe, index,h) : 
    
    if(index>=len(st)) or ss>se:
        return
  
    global stack
    # If segment of this node is a part  
    # of given range, then return  
    # the min of the segment  
    if (qs <= ss and qe >= se) : 
        if(stack==[] or h[stack[-1][1]]<h[ss]):
            stack.append((ss,se,st[index]))
            return 
             
  
    # If segment of this node  
    # is outside the given range  
    if (se < qs or ss > qe) : 
        return 
  
    # If a part of this segment  
    # overlaps with the given range  
    mid = getMid(ss, se); 
     
    RMQUtil(st, ss, mid,qs,qe, 2 * index + 1,h) 
    RMQUtil(st, mid + 1,se,qs, qe, 2 * index + 2,h)
  
# Return minimum of elements in range  
# from index qs (query start) to  
# qe (query end). It mainly uses RMQUtil()  

def range1(st,n,l,r,h):

    return RMQUtil(st, 0, n - 1, l, r, 0,h)
    
    
    
    




def solveQuery(a,h,s,d):
    
    global stack
    if(d<s):
        if(s==d):
            return a[s]
   
        if(h[s]<=h[d]):
            return -1
        #left to right
        
        
        stack=[]
        range1(st,n,d,s,h)
        # print stack
        if(stack==[] or stack[0][0]!=d or stack[-1][1]!=s):
            #print stack,stack[0][0],stack[-1][1]
            return -1
        sum1=0
        for i in stack:
            sum1+=i[2]
        return sum1

    #right to left
    else:
        if(s==d):
            return a[::-1][n-s-1]
   
        if(h[n-s-1]<=h[n-d-1]):
            return -1
        # print "h inverse",h[::-1]
        # print "a inverse",a[::-1]
        # print "right to left",n-d,n-s
        stack=[]
        range1(st2,n,n-d-1,n-s-1,h[::-1])
        # print stack
        if(stack==[] or stack[0][0]!=n-d-1 or stack[-1][1]!=n-s-1):
            #print stack,stack[0][0],stack[-1][1]
            return -1
        sum1=0
        for i in stack:
            sum1+=i[2]
        return sum1
                

for i in range(q):
    x,s,d=map(int,raw_input().split())
    if(x==2):
                
        #if source is greater then destination then only move to next
        #min and max possible height
        print solveQuery(a,h,s-1,d-1)
    else:
        #here update st
        a[s-1]=d
        
        st = [-1] * (max_size);  
        st2=[-1] * (max_size);  
        constructSegmentTree(h,a,st,0,n-1,0)
        constructSegmentTree(h[::-1],a[::-1],st2,0,n-1,0)
        
    