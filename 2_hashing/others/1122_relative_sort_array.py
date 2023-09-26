from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr2)
        order = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (order.get(x, n), x))