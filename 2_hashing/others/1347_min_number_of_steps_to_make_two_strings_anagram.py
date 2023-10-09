from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ct_s = Counter(s)
        ct_t = Counter(t)
        ans = 0

        for key in ct_s:
            if ct_s[key] > ct_t[key]:
                ans += ct_s[key] - ct_t[key]

        return ans