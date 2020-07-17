
#learn fenwick tree : https://www.hackerearth.com/practice/notes/binary-indexed-tree-or-fenwick-tree/#c217533

#step1
n=8
#should be 2
firtSetBitBinary=n&(-n)
#gives the value of binary number equalivalent to n with only lsq bit set
print firtSetBitBinary

#cool trick to call a lambda function in python
sum=lambda x,y : x+y
print sum(1,2)