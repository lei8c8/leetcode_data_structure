import collections

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1
        current_sum, ans = 0, 0
        for num in nums:
            current_sum += num
            ans += d[current_sum - goal]
            d[current_sum] += 1
        return ans