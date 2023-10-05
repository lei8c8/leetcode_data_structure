from collections import defaultdict

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        dd = defaultdict(int)

        for num in nums:
            if num % 2 == 0:
                dd[num] += 1

        if not dd:
            return -1

        freq = max(dd.values())
        ans = float('inf')
        
        for key in dd:
            if dd[key] == freq:
                ans = min(ans, key)
        return ans
