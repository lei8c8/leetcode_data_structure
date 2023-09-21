class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        unique = len(set(candyType))
        if unique < n // 2:
            return unique
        return n // 2