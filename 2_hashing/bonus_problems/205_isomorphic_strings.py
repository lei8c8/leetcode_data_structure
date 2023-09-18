class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_map = dict()
        t_to_s_map = dict()

        for c1, c2 in zip(s, t):
            if c1 not in s_to_t_map and c2 not in t_to_s_map:
                s_to_t_map[c1] = c2
                t_to_s_map[c2] = c1
            elif s_to_t_map.get(c1) != c2 or t_to_s_map[c2] != c1:
                return False
        
        return True
