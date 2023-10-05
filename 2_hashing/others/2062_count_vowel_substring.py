class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        vowel = set('aeiou')

        for start in range(len(word)):
            seen = set()
            for end in range(start, len(word)):
                if word[end] in vowel:
                    seen.add(word[end])
                    if seen == vowel:
                        ans += 1
                else:
                    break
        
        return ans