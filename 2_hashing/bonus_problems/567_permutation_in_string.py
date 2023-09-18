from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False

        ct1 = Counter(s1)
        ct2 = Counter(s2[:m])

        if ct1 == ct2:
            return True

        for i in range(m, n):
            ct2[s2[i]] += 1
            ct2[s2[i - m]] -= 1
            if ct2[s2[i - m]] == 0:
                del ct2[s2[i - m]]

            if ct1 == ct2:
                return True

        return False