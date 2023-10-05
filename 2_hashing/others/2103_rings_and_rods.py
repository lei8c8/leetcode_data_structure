from collections import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        dd = defaultdict(set)

        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i + 1]
            dd[rod].add(color)

        ans = 0
        for v in dd.values():
            if len(v) == 3:
                ans += 1
        return ans