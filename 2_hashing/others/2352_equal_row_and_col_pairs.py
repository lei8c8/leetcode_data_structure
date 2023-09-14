from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_ct, col_ct, n, ans = defaultdict(int), defaultdict(int), len(grid), 0

        for row in grid:
            row_ct[tuple(row)] += 1

        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            col_ct[tuple(col)] += 1

        for key in row_ct:
            ans += row_ct[key] * col_ct[key]

        return ans
        