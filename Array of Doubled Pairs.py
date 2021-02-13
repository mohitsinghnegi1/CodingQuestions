# Qus:https://leetcode.com/problems/array-of-doubled-pairs/

# bad solution lot of corner cases
"""
    Intution :
    sort number in Dec order
    when  you find no matching pair return False
    else remove both entries from arr until arr gets empty
    (Corner case for -ve number (4/2 =2 correct) but for -ve number -2/2 =-1 which is greater then 2 we want half of it which is 4

"""

from collections import defaultdict, Counter


class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if(arr == []):
            return True
        if(arr.count(0) % 2 != 0):
            return False

        arr.sort(reverse=True)
        print arr
        i = 0
        while(True):
            if(len(arr) == 0):
                return True
            if(i < len(arr)):
                # print arr[i]%2,(arr[i]/2),arr
                if(arr[i] % 2 == 0 and arr[i] >= 0 and (arr[i]/2) in arr):
                    temp = arr[i]
                    arr.pop(i)
                    arr.remove(temp/2)
                elif(arr[i] < 0 and (arr[i]*2) in arr):
                    temp = arr[i]
                    arr.pop(i)
                    arr.remove(temp*2)
                else:
                    # print arr
                    return False

        return True


class Solution2(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if(arr == []):
            return True

        counter = Counter(arr)

        print sorted(arr, key=abs)

        for i in sorted(arr, key=abs):
            if(counter[i] == 0):
                continue
            if(counter[i*2] == 0):
                return False
            counter[i] -= 1
            counter[i*2] -= 1
        return True
