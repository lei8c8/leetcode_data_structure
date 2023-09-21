from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:

        def match_plate(word):
            ct_copy = ct.copy()
            for c in word:
                if c in ct_copy:
                    ct_copy[c] -= 1
            return all(v <= 0 for v in ct_copy.values())
        
        ct = Counter(c.lower() for c in licensePlate if c.isalpha())
        words.sort(key=len)
        for word in words:
            if match_plate(word):
                return word

