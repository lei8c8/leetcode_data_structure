class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len({num for num in nums if num})
