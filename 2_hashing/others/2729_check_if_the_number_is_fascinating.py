from collections import Counter

class Solution:
    def isFascinating(self, n: int) -> bool:
        number = str(n)
        twice = str(2 * n)
        triple = str(3 * n)
        result = number + twice + triple
        ct = Counter(result)

        if '0' in ct:
            return False

        for c in range(1, 10):
            if ct[str(c)] != 1:
                return False
        return True
        