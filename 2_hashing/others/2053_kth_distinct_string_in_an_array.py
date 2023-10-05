from collections import Counter

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        ct = Counter(arr)
        ans = ""

        i = 0
        for ele in arr:
            if ct[ele] == 1:
                i += 1
            if i == k:
                return ele
            
        return ans
        