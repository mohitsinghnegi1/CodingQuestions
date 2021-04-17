# QUs:https://leetcode.com/problems/partition-equal-subset-sum/

# brute force - tle
def par(nums, half, i, sum1=0, sum2=0):
    global ans
    if(not ans):

        if(sum1 > half or sum2 > half):
            return False

        if(i >= len(nums)):
            if(sum1 == sum2):
                ans = True
            return

        # take and add nums[i] to sum1
        par(nums, half, i+1, sum1+nums[i], sum2)

        # donttake and add nums[i] to sum2
        par(nums, half, i+1, sum1, sum2+nums[i])


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # take don't take concept
        global ans
        ans = False

        total = sum(nums)

        if(total % 2):
            return False

        par(nums, total/2, 0)
        return ans


# optimal solution using 2d array O(n^n)

class Solution2(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # construct a dp 2d array  with row representing number of element we have from 0 ..i
        # col represent sum up to half of the array
        # where each cell represent if we have element upto index i can we construct sum j

        # how we are computing each cell value ?
        # possible cases if we do not take all previous eleemnt except current index elemnt then
        # mark dp[i][nums[i]] as true
        # also all the possible sum that we can construct without elemnt at index i is also
        # possible if we are having element i
        # so dp[i][j] = true if dp[i-1][j]=true
        # also if dp[i-1][j] is true means the sum j is possible with i-1 set, adding nums[i] to
        # j will also be true dp[i][j+nums[i]]=true

        sum1 = sum(nums)

        # in case of odd sum partiotion is not possible
        if(sum1 % 2):
            return False

        nums = [None]+nums

        out = []

        for i in range(len(nums)):
            v = [True]
            for j in range(1, sum1/2+1):
                v.append(False)
            out.append(v)

        # for i in out:
        #     print i

        for i in range(1, len(nums)):
            for j in range(1, sum1/2+1):
                out[i][j] = out[i -
                                1][j] or (out[i-1][j-nums[i]]) if (j-nums[i] >= 0) else False

        return out[-1][-1]


# tle revision

class Solution3(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if(total % 2):
            return False

        def subset(nums, i, sum1, total):

            if(i >= len(nums)):
                return False

            if(sum1 == total/2):
                return True

            if(sum1 > total/2):
                return False

            # include
            a = subset(nums, i+1, sum1+nums[i], total)

            # exclude
            b = subset(nums, i+1, sum1, total)

            return a or b

        return subset(nums, 0, 0, total)


class Solution4(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if(total % 2):
            return False

        matrix = [[False for j in range(sum(nums)/2+1)]
                  for i in range(len(nums)+1)]
        # print matrix
        matrix[0][0] = True

        nums = [0]+sorted(nums)
        for i in range(len(nums)):

            # we dont care how many items are there we can always form sum = 0
            matrix[i][0] = True

        # matrix[i][j] = i element j th sum is this possible -- kya possible hai first i element ko use karke j sum banana

        # print matrix
        for i in range(len(nums)):
            # we have only i items

            for j in range(1, sum(nums)/2+1):
                # we need to make j sum is this possible

                # take  -- if we take item i can we form j sum
                if(j-nums[i] >= 0):
                    # i am doing i -1 bec we need to pick the item first time
                    matrix[i][j] = matrix[i-1][j-nums[i]]
                    # so we must not pick it second it matrix[i][j-nums[i]] means someone might already have pickked i item
                    # so always use i-1 if non repeated

                # dont take -- if we dont take item i can we form sum j
                matrix[i][j] = matrix[i][j] or matrix[i-1][j]

                # if(i==2 and j==6):
                #     print j-nums[i],2,1
                #     print matrix[i][j]
        print matrix
        return matrix[-1][-1]
