import re

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        ct = {}

        for word in re.split(' ', s1):
            ct[word] = ct.get(word, 0) + 1

        for word in re.split(' ', s2):
            ct[word] = ct.get(word, 0) + 1

        return [k for k in ct if ct[k] == 1]