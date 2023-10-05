class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        counts, n = {}, len(words)

        for word in words:
            for c in word:
                counts[c] = counts.get(c, 0) + 1

        for key in counts:
            if counts[key] % n != 0:
                return False
        
        return True
        