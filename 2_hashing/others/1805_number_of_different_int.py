import re

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len({int(d) for d in re.findall(r'\d+', word)})
            
        