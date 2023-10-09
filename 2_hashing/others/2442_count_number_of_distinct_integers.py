class Solution:
    def countDistinctIntegers(self, nums):
        reversed_nums = [int(str(num)[::-1]) for num in nums]
        nums += reversed_nums
        return len(set(nums))