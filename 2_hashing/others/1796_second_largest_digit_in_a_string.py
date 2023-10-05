class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for c in s:
            if c.isdigit():
                digits.add(int(c))
        return sorted(digits)[-2] if len(digits) >= 2 else -1