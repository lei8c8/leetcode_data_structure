class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_keys = set(brokenLetters)
        
        def can_type(word):
            return 0 if any(c in broken_keys for c in word) else 1
        
        return sum(can_type(word) for word in text.split())
        