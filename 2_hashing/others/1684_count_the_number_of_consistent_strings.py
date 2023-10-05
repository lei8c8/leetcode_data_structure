class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        ans = 0

        for word in words:
            valid = True
            for c in word:
                if c not in allowed_set:
                    valid = False
                    break
            if valid:
                ans += 1

        return ans