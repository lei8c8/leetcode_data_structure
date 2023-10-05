from collections import Counter

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        return all(v % 2 == 0 for v in Counter(nums).values())
        