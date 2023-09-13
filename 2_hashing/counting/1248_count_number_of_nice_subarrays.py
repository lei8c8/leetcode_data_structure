from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums, k):
        counts = defaultdict(int)
        counts[0] = 1
        curr = 0
        ans = 0

        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1

        return ans