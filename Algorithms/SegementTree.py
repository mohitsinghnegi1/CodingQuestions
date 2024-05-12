# Resource: https://www.youtube.com/watch?v=-dUiRtJ8ot0
import sys
class SegmentTree(object):

    def __init__(self,arr):
        self.arr = arr
        self.n = len(self.arr)
        self.seg_tree = [0]*4*self.n

    def build(self,seg_root_idx,lower,upper):
        # what to pass an argument ?
        # here 0 means 0th index of segment tree

        # we know that seg_index 0 will contain answwer to complete range
        print(f"seg_root_idx {seg_root_idx},lower {lower} ,upper {upper}")
        # base case ie when lower==uper
        if(lower==upper):
            # print("lower",lower,seg_root_idx)
            self.seg_tree[seg_root_idx] = self.arr[lower]
            return self.seg_tree[seg_root_idx]


        # create left and right branch
        mid = (lower+upper)//2

        left_seg = self.build(2*seg_root_idx+1,lower,mid) # the segment size is decreasing as we can see
        # left segment value is set

        right_seg = self.build(2*seg_root_idx+2,mid+1,upper) # the segment size is decreasing as we can see
        # right segment value is set
        # we actually dont need to return the segment value as it is passed by regference

        # segemnt value at index seg_root_idx is noting but the min , max , sum, product etc.
        # add it here

        self.seg_tree[seg_root_idx] = max(left_seg,right_seg)
        return self.seg_tree[seg_root_idx]

    def range_query(self,query_lower,query_upper,seg_root_idx,lower,upper):
        # How to decide the param ? for query you just need to know that whatever we pass in build , additionally
        # we need to pass query_lower and query_upper

        # remember their are three conditions
        print(f"query_lower {query_lower}, query_upper {query_upper} , seg_root_idx {seg_root_idx},lower {lower} ,upper {upper}")
        # partial overlap or within
        # Note Always keep these two condition as base condition in initial
        # complete overlap
        if(query_lower<=lower<=upper<=query_upper):

            return self.seg_tree[seg_root_idx]

        if(query_upper<lower or upper< query_lower):
            # no overlap
            return -sys.maxsize

        # move in both directions  (partial overlap or complete within)
        mid = (lower+upper)//2

        left_max = self.range_query(query_lower,query_upper,2*seg_root_idx+1,lower,mid)
        right_max = self.range_query(query_lower,query_upper,2*seg_root_idx+2,mid+1,upper)

        return max(left_max,right_max)

    def update(self,seg_root_idx,lower,upper,arr_idx):

        if(lower==upper):
            self.seg_tree[seg_root_idx] = self.arr[lower]
            return

        mid = (lower+upper)//2

        if(arr_idx<=mid):
            self.build(2*seg_root_idx+1,lower,mid) # the segment size is decreasing as we can see
        else:
            self.build(2*seg_root_idx+2,mid+1,upper) # the segment size is decreasing as we can see

        self.seg_tree[seg_root_idx] = max(self.seg_tree[2*seg_root_idx+1],self.seg_tree[2*seg_root_idx+2])



arr = [0,1,2,3,4,5]
n = len(arr)
st = SegmentTree(arr)
st.build(0,0,n-1)
print(st.seg_tree)
print(st.range_query(1,3,0,0,n-1))
st.arr[2]=3
st.update(0,0,n-1,2)
print(st.range_query(1,2,0,0,n-1))
print(st.range_query(2,3,0,0,n-1))















