from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        dd = defaultdict(list)
        for i, v in enumerate(groupSizes):
            dd[v].append(i)
        for k in dd:
            for i in range(0, len(dd[k]), k):
                ans.append(dd[k][i:i+k])
        return ans

