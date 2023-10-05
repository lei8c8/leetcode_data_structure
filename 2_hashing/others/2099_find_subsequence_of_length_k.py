class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        nums_with_index = [(v, i) for i, v in enumerate(nums)]
        nums_with_index.sort(key=lambda x: (-x[0], x[1]))
        return [ele[0] for ele in sorted(nums_with_index[:k], key=lambda x: x[1])]