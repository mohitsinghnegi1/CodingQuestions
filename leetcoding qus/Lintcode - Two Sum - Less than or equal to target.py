# Qus: https://allen1128.gitbooks.io/daily-work/content/two-sum-less-than-or-equal-to-target.html
def twoSum5(nums, target):
    if (len(nums) == 0):
        return 0

    nums.sort()

    count = 0
    left = 0
    right = len(nums) - 1

    while (left < right):
        if(nums[left] + nums[right] < target):
            count += (right - left)
            left += 1
        else:
            right -= 1

    return count


print twoSum5([2, 7, 11, 15], 24)
