class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        curr = s[:k]
        ans = 1 if num % int(curr) == 0 else 0
        for right in range(k, len(s)):
            left = right - k + 1
            curr = s[left:right + 1]
            try:
                if num % int(curr) == 0:
                    ans += 1
            except:
                pass
        return ans