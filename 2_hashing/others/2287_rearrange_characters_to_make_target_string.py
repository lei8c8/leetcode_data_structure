from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans = float('inf')
        s_ct = Counter(s)
        t_ct = Counter(target)

        for k in t_ct:
            ans = min(ans, s_ct[k] // t_ct[k])
        
        return ans