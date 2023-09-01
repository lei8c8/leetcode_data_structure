from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [self.nums[0]]
        for i in range(1, len(self.nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]
        return self.prefix_sum[right]
        