
'''
Qus:https://discuss.codechef.com/t/google-online-coding-challenge-internship-2021-cutoff-score-how-many-question-req/75163
Test cases

1
8
16 17 12 7 20 18 7 8
6 8
3 8
8 1 
2 7
2 3 
7 5
2 4


'''

from collections import defaultdict
from fractions import gcd #gcd module is in fraction module in python 2
# from math import gcd  #this is in python3

def getChildparent(idx,d,d2,par=None):
    
    d2[idx]=par
    
    for i in d[idx]:
        #dont go back to parent
        if(i!=par):
            getChildparent(i,d,d2,idx)

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,raw_input().split()))
    d=defaultdict(list)
    for i in range(n-1):
        u,v=map(int,raw_input().split())
        #since i am using 0 based indexing 
        d[u-1].append(v-1)
        d[v-1].append(u-1)
        
    #now dict is created 
    # we need to get child parent relationship dict
    d2={}
    #parent of 0th node is None
    d2[0]=None
    
    # this function will return a dictionary of child parent relationship
    getChildparent(0,d,d2)
    
    print d2
    
    
    #to handle no coprime case we have initialized this array with -1
    out=[-1]*n
    
    for i in d2:
        par=d2[i]#index of par
        while(par):
            if(gcd(a[par],a[i])==1):
                out[i]=par+1 #since in qus it is one based indexing
                break
            par=d2[par]

    print " ".join(map(str,out))
        
    
    
        