import collections

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        ct = collections.Counter(nums)
        return sum(x for x in ct if ct[x] == 1)