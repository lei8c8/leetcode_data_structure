class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans, n = "", len(s)
        for i in range(n - 1):
            for j in range(i + 1, n):
                lookup = set(s[i:j+1])
                if len(lookup) % 2 != 0:
                    continue
                if all(c.swapcase() in lookup for c in s[i:j+1]):
                    if len(s[i:j+1]) > len(ans):
                        ans = s[i:j+1]
        return ans