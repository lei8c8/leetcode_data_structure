from collections import defaultdict

class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        dd = defaultdict(int)

        for c in candidates:
            b = bin(c)[2:][::-1]
            for i, v in enumerate(b):
                if v == '1':
                    dd[i] += 1

        return max(dd.values())