from typing import List
from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        def add_items(items):
            for item in items:
                value, weight = item[0], item[1]
                dd[value] += weight

        dd = defaultdict(int)
        add_items(items1)
        add_items(items2)
        ans = []
        for key in sorted(dd):
            ans.append([key, dd[key]])
        return ans
        

        