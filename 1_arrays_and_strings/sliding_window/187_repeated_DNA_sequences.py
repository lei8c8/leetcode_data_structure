from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10:
            return []
        
        ct = defaultdict(int)
        for right in range(10, len(s) + 1):
            left = right - 10
            ct[s[left:right]] += 1

        return [key for key in ct if ct[key] > 1]


