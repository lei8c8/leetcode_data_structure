from collections import defaultdict

class Solution:
    def longestCommonSubsequence(self, arrays: list[list[int]]) -> list[int]:
        dd = defaultdict(int)
        rows = len(arrays)

        for row in arrays:
            for ele in row:
                dd[ele] += 1

        return [x for x in dd if dd[x] == rows]