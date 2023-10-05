class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_idx = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_idx.add(i)

        if len(diff_idx) == 1 or len(diff_idx) > 2:
            return False
        elif not diff_idx:
            return True
        else:
            i = diff_idx.pop()
            j = diff_idx.pop()
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
            else:
                return False
