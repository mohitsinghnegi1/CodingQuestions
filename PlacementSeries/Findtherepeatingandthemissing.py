# QUs: https: // www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

# Input: arr[] = {3, 1, 3}
# Output: Missing = 2, Repeating = 3

# first method is purely equation based

from functools import reduce
a = map(int, raw_input().split())
n = len(a)
p = reduce(lambda x, y: x*y, [i for i in range(1, n+1)])

s = n*(n+1)/2

gs = sum(a)
gp = reduce(lambda x, y: x*y, [i for i in a])

# x is missing number y is repeating number
# gs = s+y-x
# gp = p*y/x

# x = p*y/gp
# y=x*gp/p


print s, p, gs, gp

# x = s+(x*gp)/p-gs
# x-(x*gp)/p = s-gs
x = ((s-gs)*p)/(p-gp)

print "missing number", x

y = x*gp/p

print "dublicate number", y


# second method using xor -- efficient one

# 1) do xor of 1 to n  say it xor1ton
# 2) do xor of givn array say xorArr
# 3) on xor of xor1ton and xorArr  we are left with x ^ y  --incomplete
# 4) seperate given array number into two buckets one bucket with set bit and other dont hve set bit
# 5) now again triverse frm 1 to n and insrt set bit at same pos in 1 bucket and other in 2nd bucket
# 6) xor both the bucket you will get two number . one of them will be a missing and other will be a dublicate number
# 7) now again triverse into the array to find which number is missing nd which number is dublicate


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # this contain 1, n number except a missing number and a duplicate number

    x = reduce(lambda x, y: x ^ y, a)
    y = reduce(lambda x, y: x ^ y, range(1, n+1))
    xXorY = x ^ y

    # now we have x^y we have to sepearate them to get their values
    # how to do it?
    # we know 1^1 ==0 and  0^0=0 and 1^0==0 and 0^1==0
    # We know x and y is a different number so there will be one set bit
    # in xXorY at position pos, which means one of the number(missing or repeated)
    # have set bit on pos position
    # we can use this info to create two bucket one is having all the number
    # having set bit at pos and one bucket will have all number with off bit
    # at pos
    # print("bin",bin(xXorY))

    # pos = bin(xXorY)[::-1].index('1')
    pos = xXorY & ~(xXorY-1)

    bucket1 = bucket2 = 0

    # how we can get a first set bit?
    # using x~(x-1) we can get a binary representation of first set bit
    # for val in a:
    #     if(pos < len(bin(val)) and bin(val)[::-1][pos] == '1'):
    #         bucket1 ^= val
    #     else:
    #         bucket2 ^= val

    # for val in range(1, n+1):
    #     if(pos < len(bin(val)) and bin(val)[::-1][pos] == '1'):
    #         bucket1 ^= val
    #     else:
    #         bucket2 ^= val

    for j in range(len(a)):

        # was doing mistake instead of using set bit i was usinf xXorY
        if(a[j] & pos):

            bucket1 ^= a[j]
        else:
            bucket2 ^= a[j]

    for i in range(1, n+1):

        if(i & pos):
            bucket1 ^= i
        else:
            bucket2 ^= i

    print(bucket2, bucket1) if a.count(bucket2) > 1 else print(bucket1, bucket2)
