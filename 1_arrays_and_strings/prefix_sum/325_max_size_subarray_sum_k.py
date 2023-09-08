class Solution:
    def maxSubArrayLen(self, nums, k: int) -> int:
        ans, curr, prefix_sum = 0, 0, {0: 0}
        for i,v in enumerate(nums):
            curr += v
            if curr not in prefix_sum:
                prefix_sum[curr] = i + 1
            if curr - k in prefix_sum:
                ans = max(ans, i - prefix_sum[curr - k] + 1)
        return ans
        