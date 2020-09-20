# Qus:https://leetcode.com/problems/counting-bits/
# time complexity O(1)

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        out = [0, 1]

        if(num < 2):
            return out[:num+1]

        pPow = 0
        nPow = 2

        # how to approach this problem
        # for every elemnt we will check what is the previous power of 2
        # substract it from the number getting the number of 1 in the remaining number say this no is         #Rem so our ans for out[no]=out[prevPowOf2]+out[no-prevPowOf2] In general it means the total         #number of one is equal to number of 1 in last power of 2 plus the number of 1 in                   #number2 that we get after substracting last power of 2 from i
        # example    (no of 1 in 13) = (number of 1 in 8 + number of 1 in 5)

        for i in range(2, num+1):
            if(i == nPow):

                out.append(1)
                pPow = nPow
                nPow = nPow << 1

            else:
                out.append(1+out[i-pPow])

        return out
