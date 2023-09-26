from collections import Counter

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        to_delete = set()
        n = len(words)
        i = n - 1
        while i > 0:
            if Counter(words[i]) == Counter(words[i - 1]) :
                to_delete.add(i)
            i -= 1
        return [words[i] for i in range(n) if i not in to_delete]