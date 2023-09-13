from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        ct1, ct2 = Counter(word1), Counter(word2)

        for key in ct1:
            if abs(ct1[key] - ct2[key]) > 3:
                return False
            
        for key in ct2:
            if abs(ct1[key] - ct2[key]) > 3:
                return False
            
        return True


class Solution2:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26

        for i in range(len(word1)):
            arr1[ord(word1[i]) - ord('a')] += 1
            arr2[ord(word2[i]) - ord('a')] += 1

        for i in range(26):
            if abs(arr1[i] - arr2[i]) > 3:
                return False
            
        return True