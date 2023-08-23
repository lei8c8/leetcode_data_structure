class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        seen, ans, left = set(), 0, 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans += (right - left + 1)
        return ans
