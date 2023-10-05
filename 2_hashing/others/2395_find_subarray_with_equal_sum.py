class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        s = set()
        for i in range(1, len(nums)):
            sub_sum = nums[i - 1] + nums[i]
            if sub_sum in s:
                return True
            s.add(sub_sum)
        return False
