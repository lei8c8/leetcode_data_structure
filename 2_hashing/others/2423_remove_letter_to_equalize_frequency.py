from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        ct = Counter(word)

        for c in word:
            ct[c] -= 1
            if ct[c] == 0:
                del ct[c]
            if len(set(ct.values())) == 1:
                return True
            ct[c] += 1
        
        return False
            