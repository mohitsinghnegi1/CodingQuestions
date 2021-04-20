# Qus:https://www.codechef.com/COOK128B/problems/OROFAND
# Editorial :https://discuss.codechef.com/t/orofand-editorial/88251
"""
2
3 2
1 2 3
1 4
3 0
4 1
1 2 3 4
4 0

"""


def removeBit(val, bitFreq):
    i = 0
    while(i < 32):
        bitFreq[i] -= (1 if (val & (1 << i)) else 0)
        i += 1


def addBit(val, bitFreq):
    i = 0
    while(i < 32):
        bitFreq[i] += (1 if (val & (1 << i)) else 0)
        i += 1
    # print "after adding bit ", bitFreq


def getBinary(bitFreq):

    binary = ''
    for i in range(31, -1, -1):
        binary += ('1' if bitFreq[i] > 0 else '0')
    # print binary
    return binary


def findArrBitFrequency(a):

    bitFreq = {}
    for i in range(32):
        bitFreq[i] = 0

    for val in a:
        i = 0
        while(i < 32):
            bitFreq[i] += (1 if (val & (1 << i)) else 0)
            i += 1
    return bitFreq


t = int(input())
for i in range(t):
    n, q = map(int, raw_input().split())
    a = map(int, raw_input().split())

    bitFreq = findArrBitFrequency(a)
    print int(getBinary(bitFreq), 2)
    for i in range(q):
        x, v = map(int, raw_input().split())
        removeBit(a[x-1], bitFreq)
        # print ">>>> remove Bit", a[x-1], int(getBinary(bitFreq), 2)
        addBit(v, bitFreq)
        # print ">>>> add Bit", v, int(getBinary(bitFreq), 2)
        print int(getBinary(bitFreq), 2)
        a[x-1] = v
