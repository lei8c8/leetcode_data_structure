from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()

        for r in ranges:
            start, end = r[0], r[1]
            for i in range(start, end + 1):
                covered.add(i)
        
        for num in range(left, right + 1):
            if num not in covered:
                return False
        return True