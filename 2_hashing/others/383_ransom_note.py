import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        ct = collections.Counter(magazine)

        for ch in ransomNote:
            ct[ch] -= 1
            if ct[ch] < 0:
                return False
        
        return True


if __name__ == '__main__':
    solution = Solution()
    re = solution.canConstruct('aa', 'aab')
    print(re)