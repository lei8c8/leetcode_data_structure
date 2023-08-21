class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        ct= {}
        for i in range(3):
            ct[s[i]] = ct.get(s[i], 0) + 1
        ans = 1 if len(ct) == 3 else 0

        for i in range(3, len(s)):
            ct[s[i]] = ct.get(s[i], 0) + 1
            ct[s[i - 3]] -= 1
            if ct[s[i - 3]] == 0:
                del ct[s[i - 3]]
            if len(ct) == 3:
                ans += 1
        return ans
        



