class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        seen = set()

        for right in range(len(s)):
            ch = s[right]
            while ch in seen:
                seen.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)
            seen.add(ch)

        return ans