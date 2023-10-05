class Solution:
    def digitCount(self, num: str) -> bool:
        ct = {}
        for c in num:
            ct[c] = ct.get(c, 0) + 1
        for i in range(len(num)):
            if ct.get(str(i), 0) != int(num[i]):
                return False
            
        return True