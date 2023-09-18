class Solution:
    def customSortString(self, order: str, s: str) -> str:
        custom_order = {}
        for i, v in enumerate(order):
            custom_order[v] = i
        ans = sorted(s, key=lambda x: custom_order.get(x, len(s)))
        return ''.join(ans)
    

from collections import Counter

class Solution2:
    def customSortString(self, order: str, s: str) -> str:
        ans, ct = [], Counter(s)

        for ch in order:
            ans.append(ch * ct[ch])
            del ct[ch]

        for ch in ct:
            ans.append(ch * ct[ch])

        return ''.join(ans)
    

       