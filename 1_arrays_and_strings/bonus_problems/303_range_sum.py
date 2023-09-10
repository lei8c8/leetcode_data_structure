class NumArray:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sumRange(self, left, right):
        return self.prefix_sum[right] - self.prefix_sum[left] + self.nums[left]
    


class NumArray2:
    def __init__(self, nums) -> None:
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left] 