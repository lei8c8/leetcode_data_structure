class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        window_start, ans, ct, n = 0, 0, {}, len(s)
        for window_end in range(n):
            ct[s[window_end]] = ct.get(s[window_end], 0) + 1
            while len(ct) == 3:
                ans += n - window_end
                ct[s[window_start]] -= 1
                if ct[s[window_start]] == 0:
                    del ct[s[window_start]]
                window_start += 1
        return ans
            

