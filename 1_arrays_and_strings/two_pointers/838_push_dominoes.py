class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        idx_list = [(-1, 'L')] + [(i, v) for i, v in enumerate(dominoes) if v != '.'] + [(len(dominoes), 'R')]
        ans = list(dominoes)
        for idx in range(len(idx_list) - 1):
            i, x = idx_list[idx]
            j, y = idx_list[idx + 1]
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x == 'R' and y == 'L':
                left = i + 1
                right = j - 1
                while left < right:
                    ans[left] = 'R'
                    ans[right] = 'L'
                    left += 1
                    right -= 1
        return ''.join(ans)