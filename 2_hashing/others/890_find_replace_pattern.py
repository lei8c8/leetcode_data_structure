class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        
        def match(word):
            map1, map2 = {}, {}
            for x, y in zip(word, pattern):
                if x not in map1:
                    map1[x] = y
                if y not in map2:
                    map2[y] = x
                if map1[x] != y or map2[y] != x:
                    return False
            return True
        
        return [word for word in words if match(word)]
        



        


