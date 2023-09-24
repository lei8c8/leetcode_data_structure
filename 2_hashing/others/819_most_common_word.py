import re
from string import punctuation
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        def to_lower_case_and_remove_puntuation(word):
            if word[-1] in punctuation:
                word = word[:-1]
            word = word.lower()
            return word
        
        banned_set = set(banned)
        counter = defaultdict(int)

        for word in re.split(',| ', paragraph):
            if word:
                word = to_lower_case_and_remove_puntuation(word)
                counter[word] += 1

        for key in sorted(counter, key=lambda x: -counter[x]):
            if key not in banned_set:
                return key
            
        return ""

        
