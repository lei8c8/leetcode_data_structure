from collections import defaultdict

class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        dd = defaultdict(int)

        for word in words:
            key = min(word, word[::-1])
            dd[key] += 1

        ans = 0 
        for v in dd.values():
            ans += v * (v -1)

        return ans // 2