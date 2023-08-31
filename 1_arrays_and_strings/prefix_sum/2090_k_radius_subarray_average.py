from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])

        ans = [-1] * len(nums)
        for i in range(n):
            if i < k or i > n - k - 1:
                continue
            curr_sum = prefix_sum[i + k] - prefix_sum[i - k] + nums[i - k]
            ans[i] = curr_sum // (2 * k + 1)
        
        return ans
