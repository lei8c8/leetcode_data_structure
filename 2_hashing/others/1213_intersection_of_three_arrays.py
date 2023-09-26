from typing import List
from collections import Counter

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ct = Counter(arr2) + Counter(arr3)
        return [x for x in arr1 if ct[x] == 2]