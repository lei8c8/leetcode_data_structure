class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        ans, ct = 0, {}
        for x, y in dominoes:
            key = tuple(sorted([x, y]))
            if key in ct:
                ans += ct[key]
            ct[key] = ct.get(key, 0) + 1
        return ans