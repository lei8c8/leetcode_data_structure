from math import gcd
from functools import reduce
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        ct = Counter(deck)
        return reduce(gcd, ct.values()) >= 2
        