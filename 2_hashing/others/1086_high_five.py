from typing import List
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ans = []
        dd = defaultdict(list)

        for student_id, score in items:
            dd[student_id].append(score)

        for student_id in sorted(dd):
            dd[student_id].sort(reverse=True)
            ans.append([student_id, sum(dd[student_id][:5]) // 5])

        return ans
