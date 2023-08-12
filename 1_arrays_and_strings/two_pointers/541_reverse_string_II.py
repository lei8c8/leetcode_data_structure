class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans, n = [], len(s)
        requires_reverse = True

        for i in range(0, n, k):
            if not requires_reverse:
                for j in range(i, min(i + k, n)):
                    ans.append(s[j])
            else:
                for j in range(min(i + k - 1, n - 1), i - 1, -1):
                    ans.append(s[j])
            requires_reverse = not requires_reverse

        return ''.join(ans)
