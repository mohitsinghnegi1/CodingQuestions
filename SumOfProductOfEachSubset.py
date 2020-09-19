# Qus: Find the sum of product of each subset
# resource: https: // www.youtube.com/watch?v = M1q3Pzk2UXs

a = map(int, raw_input().split())

prevSum = 0
for val in a:
    nextSum = val*(prevSum+1)+prevSum
    prevSum = nextSum
print prevSum
