class Solution:
    def makePalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        diff = 0
        while left < right:
            if s[left] != s[right]:
                diff += 1
                if diff > 2:
                    return False
            left += 1
            right -= 1
        return diff <= 2