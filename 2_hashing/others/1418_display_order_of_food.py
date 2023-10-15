from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_set = set()
        food_set = set()

        for _, table_id, food in orders:
            table_set.add(int(table_id))
            food_set.add(food)

        ans = defaultdict(dict)
        for key in table_set:
            for f in food_set:
                ans[key][f] = 0

        for _, table_id, food in orders:
            ans[int(table_id)][food] += 1

        result = ['Table'] + sorted(food_set)
        for key in sorted(ans):
            row = [str(key)]
            for f in sorted(food_set):
                row.append(str(ans[key][f]))
            result.append(row)
        return result

