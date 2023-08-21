class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, ans, curr = 0, 0, {}
        for right in range(len(s)):
            curr[s[right]] = curr.get(s[right], 0) + 1
            while len(curr) > 2:
                curr[s[left]] -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans