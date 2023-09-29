from typing import *

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i, n = 0, len(arr)
        my_map = {p[0]: p for p in pieces}

        while i < n:
            if arr[i] not in my_map:
                return False
            for ele in my_map[arr[i]]:
                if ele != arr[i]:
                    return False
                i += 1
        
        return True