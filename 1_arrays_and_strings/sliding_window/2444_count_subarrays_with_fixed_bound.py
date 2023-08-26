class Solution:
    def countSubarrays(self, nums, minK, maxK):
        ans = 0
        left_bound = min_idx = max_idx = -1 
        for i, v in enumerate(nums):
            if v > maxK or v < minK:
                left_bound = i
            if v == minK:
                min_idx = i
            if v == maxK:
                max_idx = i
            ans += max(0, min(min_idx, max_idx) - left_bound)
        return ans
            