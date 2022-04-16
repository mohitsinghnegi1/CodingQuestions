# Qus:https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/
# Resource:https://www.youtube.com/watch?v=-dUiRtJ8ot0

# concepts :
# 1. total number of nodes in a segment tree is 2n-1
# the max size of segment tree required is equal to 2* pow(h) - 1 where h = int(ceil(log(n)))


'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import sys
# Write your code here
n, q = map(int, raw_input().split())
a = map(int, raw_input().split())

# segment size at max could be 4 times more then size of given array
segTree = [0]*(4*n)

# index to segIndex mapping  (Note : we are using extra space o(n) to store index mapping)
d = {}


def build(i, j, segIndex):

    if(i == j):
        # if it is a root node ie i==j then set the value of segmentTree Node
        segTree[segIndex] = a[i]
        d[i] = segIndex
        return

    mid = (i+j)/2
    # divide the given array segment into two parts
    # this segment will store left side sum (or max based on problem)
    build(i, mid, 2*segIndex+1)
    # this segment will store right sum (or max based on problem)
    build(mid+1, j, 2*segIndex+2)

    # merging logic (Replace it with your qus logic , for example if you are finding max in a       # given range then use segTree[segIndex]=max(segTree[2*segIndex+1],segTree[2*segIndex+2])

    # backtrack and set value of segment node using its left and right segment value
    segTree[segIndex] = min(segTree[2*segIndex+1], segTree[2*segIndex+2])


# build the segment tree
build(0, n-1, 0)

# print segTree

# we have constructed the segment tree
# now we can perform query and update operation


def query(l, r, segIndex, left, right):

    # return minimum in the range l...r

    # if complete overlap the rnage reamin same , but the left right will change
    if(left >= l and right <= r):
        return segTree[segIndex]

    # if no overlap
    if(r < left or l > right):
        return sys.maxsize  # since we need to find min in a range so we are returning max

    # if partial overlap
    # move in both direction
    mid = (left+right)/2

    leftMin = query(l, r, 2*segIndex+1, left, mid)
    rightMin = query(l, r, 2*segIndex+2, mid+1, right)

    return min(leftMin, rightMin)

# we can update using same build logic


def update(x, y):

    # we are updating in segtree
    parIndex = d[x]
    segTree[parIndex] = y  # update the value
    # make sure that the min value update for parent node also
    while(parIndex):
        # what is the min value between before value and new value
        parIndex = (parIndex-1)/2
        # same logic as             # tree construction
        segTree[parIndex] = min(segTree[2*parIndex+1], segTree[2*parIndex+2])


# print d
for i in range(q):
    c, x, y = raw_input().split()

    if(c == 'u'):
        x, y = int(x), int(y)
        # update a[x]=y
        update(x-1, y)

    elif(c == 'q'):
        l, r = int(x), int(y)
        # get min in range(l,r)
        # l= left range to r right range
        # segIndex
        #
        segIndex = 0
        # use same logic as building segment tree
        left, right = 0, n-1  # this we are passing it to compare with the query range
        # we are using 0 based indexing
        print query(l-1, r-1, segIndex, left, right)


# print segTree





# 2nd solution (16 April 2022)

import sys

def query(st,l,r,ql,qr,si=0):


    # three cases
    # 1. complete overlap --> return val of node
    # 2. partial overlap -->
            # In case st node completly lies within a range then it will contibute to the ans
            # In case st node does not lies inside then return vsal which could never be the ans
            # In case of partial overlap(left or bitween or right) move in both direction


    # 3. no overlap --> just return  -sys.maxsize

    # complete overlap
    if(ql<=l and r<=qr):
        return st[si]


    # no overlap
    if(r<ql or qr<l):
        return -sys.maxsize


    # partial overlap
    # move in both direction
    mid = (l+r)/2
    maxleft = query(st,l,mid,ql,qr,2*si+1)
    maxright = query(st,mid+1,r,ql,qr,2*si+2)


    return max(maxleft,maxright)


def update(st,d,x,y):

    psi = d[x] # get the segement tree index

    st[psi] = y # update by new value


    while(psi!=0):

        psi = (psi-1)/2

        # update the value of si
        st[psi] = max(st[2*psi+1],st[2*psi+2])



class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        si = index of segment tree
        range l,r = range of which this index stores the ans

        """




        n = len(nums)
        d = {}

        st = [0]*(4*n)

        def bildSegmentTree(l,r,si=0):

            if(l==r):
                # base case where range is l,l
                st[si] = nums[l]
                d[l] = si
                return st[si]

            # we need to find the max within a range
            mid = (l+r)/2
            leftmax = bildSegmentTree(l,mid,2*si+1)
            rightmax = bildSegmentTree(mid+1,r,2*si+2)

            st[si] = max(leftmax,rightmax)

            return st[si]




        bildSegmentTree(0,n-1)

        # print query(st,0,n-1,2,4)


        # print st # st has been buit


        out = []


        for i in range(n-k+1):
            out.append(query(st,0,n-1,i,i+k-1))



        # below code is for update (Not part of this question)
        # update(st,d,2,10) # uncomment this line to see this logic in action

        print st



        return out









