import string

class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = set(s)
        for i in range(len(string.ascii_lowercase) - 1, -1, -1):
            lower_c = string.ascii_lowercase[i]
            upper_c = lower_c.upper()
            if all(c in letters for c in (lower_c, upper_c)):
                return upper_c
        return ""
        