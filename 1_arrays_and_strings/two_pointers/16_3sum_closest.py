class Solution:
    def threeSumClosest(self, nums, target):
        delta = float('inf')
        nums.sort()
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(delta):
                    delta = total - target
                if total < target:
                    left += 1
                else:
                    right -= 1
        return target + delta
