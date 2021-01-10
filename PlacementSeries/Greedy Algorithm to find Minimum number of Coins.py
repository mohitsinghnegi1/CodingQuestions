# Qus:https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
amount = int(input())
noOfnotes = 0
j = len(denominations)-1
while(amount != 0):
    if(denominations[j] <= amount):
        noOfnotes += (amount/denominations[j])
        amount = amount % denominations[j]
    else:
        j -= 1
print noOfnotes
