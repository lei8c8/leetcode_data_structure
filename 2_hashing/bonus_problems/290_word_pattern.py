class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False
        
        idx_map = {}

        for i in range(len(words)):
            p, w = pattern[i], words[i]
            if '$_' + p not in idx_map:
                idx_map['$_' + p] = i
            if '#_' + w not in idx_map:
                idx_map['#_' + w] = i
            if idx_map['$_' + p] != idx_map['#_' + w]:
                return False
            
        return True