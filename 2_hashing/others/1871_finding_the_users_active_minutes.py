from typing import List
from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        id_min_map = defaultdict(set)

        for user_id, user_time in logs:
            id_min_map[user_id].add(user_time)

        ans = [0] * k
        for v in map(len, id_min_map.values()):
            ans[v - 1] += 1
        return ans