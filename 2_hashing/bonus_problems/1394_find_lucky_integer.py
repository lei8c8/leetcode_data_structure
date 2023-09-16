import collections

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        lucky_integer = -1
        ct = collections.Counter(arr)
        for key in ct:
            if key == ct[key]:
                lucky_integer = max(lucky_integer, key)
        return lucky_integer
