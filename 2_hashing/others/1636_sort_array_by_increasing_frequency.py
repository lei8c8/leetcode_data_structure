import collections

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        ct = collections.Counter(nums)
        return sorted(nums, key=lambda x: (ct[x], -x))
        