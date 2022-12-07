def sum(*nums):
    if !nums:
        return 0
    return nums[0] + sum(*nums)

