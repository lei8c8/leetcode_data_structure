from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        ct = Counter(s)
        ans = sorted(s, key=lambda x: (-ct[x], x))
        return "".join(ans)
        