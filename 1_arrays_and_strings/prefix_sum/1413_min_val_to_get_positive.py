class Solution:
    def minStartValue(self, nums):
        prefix_sum, min_prefix_sum = 0, float('inf')
        for num in nums:
            prefix_sum += num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
        return 1 - min_prefix_sum if 1 - min_prefix_sum > 0 else 1