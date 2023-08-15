class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:        
        i, j, m, n = 0, 0, len(name), len(typed)

        while i < m and j < n:
            if name[i] == typed[j]:
                i, j = i + 1, j + 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            else:
                j += 1
        
        if i != m:
            return False
        
        while j < n:
            if typed[j] != name[-1]:
                return False
            j += 1

        return True



