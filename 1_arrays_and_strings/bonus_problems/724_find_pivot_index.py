class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        prev = 0

        for i, v in enumerate(nums):
            if prev == total - v - prev:
                return i
            prev += v

        return -1

        

