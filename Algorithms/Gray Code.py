def appendOne(arr):
    out = []
    for i in range(len(arr)-1, -1, -1):
        out.append("1"+arr[i])

    return out


def appendZero(arr):
    out = []
    for i in range(len(arr)):
        out.append("0"+arr[i])

    return out


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #  ['0',|'1'] # if n == 1
        # ['00','01',|'11','10']      # if n == 2
        # ['000','001','011','010','110','111','101','100']  #if n == 3 = 2**3 = 8

        init = ['0', '1']
        n -= 1

        while(n):

            left = appendZero(init)
            right = appendOne(init)
            # print left, right
            init = left+right
            n -= 1

        return map(lambda x: int(x, 2), init)


class Solution2(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        # left shift 1 by n places. for n =3 range will be 8
        return [i ^ (i >> 1) for i in range(1 << n)]
