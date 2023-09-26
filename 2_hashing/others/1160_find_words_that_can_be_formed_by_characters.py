from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:

        def can_be_formed(word):
            word_ct = Counter(word)
            for c in word_ct:
                if word_ct[c] > ct[c]:
                    return False
            return True

        ct = Counter(chars)
        ans = 0

        for word in words:
            if can_be_formed(word):
                ans += len(word)

        return ans
