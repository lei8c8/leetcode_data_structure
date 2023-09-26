class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        rank, start = {}, 1
        for num in sorted(set(arr)):
            rank[num] = start 
            start += 1
        return [rank[num] for num in arr]