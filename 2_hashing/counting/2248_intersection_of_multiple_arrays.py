from collections import defaultdict

class Solution:
    def intersection(self, nums):
        n = len(nums)
        ans = []
        counts = defaultdict(int)

        for row in nums:
            for ele in row:
                counts[ele] += 1

        for key in sorted(counts):
            if counts[key] == n:
                ans.append(key)

        return ans


class Solution2:
    def intersection(self, nums):
        n = len(nums)
        ans = []
        counts = defaultdict(int)

        for row in nums:
            for ele in row:
                counts[ele] += 1

        for key in counts:
            if counts[key] == n:
                ans.append(key)

        return sorted(ans)

        
