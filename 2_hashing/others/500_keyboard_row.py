class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        ans = []
        set1, set2, set3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")

        for word in words:
            if (all(c.lower() in set1 for c in word) 
                or all(c.lower() in set2 for c in word) 
                or all(c.lower() in set3 for c in word)):
                ans.append(word)

        return ans