class Solution:
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        idx_map = {v: i for i, v in enumerate(nums2)}
        return [idx_map[num] for num in nums1]