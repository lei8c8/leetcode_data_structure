import collections

class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        
        ct = collections.Counter(ranks)
        max_freq = max(ct.values())

        if max_freq >= 3:
            return "Three of a Kind"
        elif max_freq == 2:
            return "Pair"

        return "High Card"