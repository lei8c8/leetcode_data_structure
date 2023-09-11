class Solution:
    def missingNumber(self, nums):
        s = set(nums)
        for x in range(len(nums) + 1):
            if x not in s:
                return x
        return -1