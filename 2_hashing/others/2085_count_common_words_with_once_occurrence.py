from collections import Counter

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        ct1 = Counter(words1)
        ct2 = Counter(words2)
        return sum(1 for key in ct1 if (ct1[key] == 1 and ct2[key] == 1))
        