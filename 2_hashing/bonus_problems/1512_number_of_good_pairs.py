import collections

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ct = collections.defaultdict(int)
        ans = 0
        for num in nums:
            ans += ct[num]
            ct[num] += 1
        return ans
    
