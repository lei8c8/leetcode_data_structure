class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans, d = -1, {}

        for i, v in enumerate(s):
            if v in d:
                ans = max(ans, i - d[v] -1)
            if v not in d:
                d[v] = i

        return ans