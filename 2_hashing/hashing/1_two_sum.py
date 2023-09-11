class Solution:
    def twoSum(self, nums, target):
        idx_map = {}
        
        for i, v in enumerate(nums):
            look_for = target - v
            if look_for in idx_map:
                return [idx_map[look_for], i]
            idx_map[v] = i

        return [-1, -1]