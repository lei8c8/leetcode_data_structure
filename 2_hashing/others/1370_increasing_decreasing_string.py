from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        ct = Counter(s)
        ans = []
        
        while ct:
            for c in sorted(ct):
                ans.append(c)
                ct[c] -= 1
                if ct[c] == 0:
                    del ct[c]
            for c in sorted(ct, key=lambda x: -ord(x)):
                ans.append(c)
                ct[c] -= 1
                if ct[c] == 0:
                    del ct[c]

        return ''.join(ans)