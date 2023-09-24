class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        code_array = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                      ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                      "...","-","..-","...-",".--","-..-","-.--","--.."]
        unique = {''.join(code_array[ord(c) - ord('a')] for c in word) for word in words}
        return len(unique)