import collections

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)