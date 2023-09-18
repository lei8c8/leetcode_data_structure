from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ct1, ct2 = Counter(word1), Counter(word2)
        if len(ct1) != len(ct2) or ct1.keys() != ct2.keys():
            return False
        return sorted(ct1.values()) == sorted(ct2.values)
