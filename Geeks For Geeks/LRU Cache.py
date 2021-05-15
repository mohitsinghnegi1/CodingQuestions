# Qus:https://practice.geeksforgeeks.org/problems/lru-cache/1

# User function Template for python3

# design the class in the most optimal way
from collections import OrderedDict


class LRUCache:

    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        # code here
        self.lruCache = OrderedDict({})
        self.cap = cap

    # Function to return value corresponding to the key.
    def get(self, key):
        # code here
        if(self.lruCache.get(key, False) != False):
            # since we have accessed this element so we need to push this element
            # to the end
            self.lruCache.move_to_end(key, last=True)

            return self.lruCache[key]
        return -1

    # Function for storing key-value pair.

    def set(self, key, value):
        # code here
        if(self.lruCache.get(key, False) != False):
            # if item already exist then just move it to the end
            self.lruCache.move_to_end(key, last=True)
            self.lruCache[key] = value  # insert new value
        else:
            # we need to insert new element which will increase the
            # capacity of the cache so we might need to evict lru item
            if(len(self.lruCache) >= self.cap):
                self.lruCache.popitem(last=False)
            self.lruCache[key] = value


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  # number of queries
        # parent child info in list
        a = list(map(str, input().strip().split()))

        lru = LRUCache(cap)

        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]

            if qtyp == 'SET':
                lru.set(int(a[i+1]), int(a[i+2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i+1])), end=' ')
                i += 2
            q += 1
        print()
# } Driver Code Ends
