# Qus:https://www.geeksforgeeks.org/check-if-array-can-be-sorted-with-one-swap/


"""
Brute Force approch :
Use sorting if there are only two number which are not in their right position  swap them and return True else return False

Timecomplexity O(n)

"""


def isSorted(a):
    for i in range(1, len(a)):
        if(a[i-1] > a[i]):
            return False
    return True


a = map(int, raw_input().split())

count = 0
first = None
second = None

for i in range(1, len(a)):
    if(a[i-1] > a[i]):
        count += 1
        if(first == None):
            first = i
        else:
            second = i

print first, second
if(count == 0):
    print True
elif(count > 2):
    print False
else:
    if(count == 1):
        a[first], a[first-1] = a[first-1], a[first]
    else:
        a[first-1], a[second] = a[second], a[first-1]

    # print a
    print isSorted(a)
