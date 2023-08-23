class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        ct, ans, left = {}, 0, 0
        for right in range(len(s)):
            ct[s[right]] = ct.get(s[right], 0) + 1

            while ct[s[right]] > 1:
                ct[s[left]] -= 1
                left += 1

            if right - left + 1 == k:
                ans += 1
                ct[s[left]] -= 1
                left += 1
        return ans