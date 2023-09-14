from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        idx_map = defaultdict(list)

        for i, v in enumerate(cards):
            idx_map[v].append(i)

        n = len(cards)
        ans = n + 1
        for k in idx_map:
            array = idx_map[k]
            if len(array) > 1:
                for i in range(len(array) - 1):
                    ans = min(ans, array[i + 1] + 1 - array[i])
        
        return ans if ans != n + 1 else -1