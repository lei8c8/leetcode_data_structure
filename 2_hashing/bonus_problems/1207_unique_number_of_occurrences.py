import collections

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        ct = collections.Counter(arr)
        return len(ct.values()) == len(set(ct.values()))