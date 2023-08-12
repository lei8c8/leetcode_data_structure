class Solution:
    def partitionLabels(self, s):
        last_idx_map = {v: i for i, v in enumerate(s)}
        start, end, ans = 0, 0, []

        for i, v in enumerate(s):
            end = max(end, last_idx_map[v])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1

        return ans
