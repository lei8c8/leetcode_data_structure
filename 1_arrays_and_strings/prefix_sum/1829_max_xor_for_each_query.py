class Solution:
    def getMaximumXor(self, nums, maximumBit):
        max_num, prefix_xor = 2 ** maximumBit - 1, [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
        return [max_num ^ prefix_xor[i] for i in range(len(nums) - 1, -1, -1)]