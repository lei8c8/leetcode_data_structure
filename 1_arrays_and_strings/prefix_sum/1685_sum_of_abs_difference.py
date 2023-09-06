from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 1)
        ans = [0] * n

        # prefix_sum[i] = sum from index 0 to i - 1
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        # suffix_sum[i] = sum from index i to n - 1
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        for i in range(n):
            ans[i] = nums[i] * i -  nums[i] * (n - 1 - i) - prefix_sum[i] + suffix_sum[i + 1]

        return ans
