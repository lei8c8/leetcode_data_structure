from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ct = Counter(s)
        odd = 0

        for key in ct:
            if ct[key] % 2 == 1:
                odd += 1

        return odd <= 1