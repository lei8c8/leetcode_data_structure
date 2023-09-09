class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        read_idx = write_idx = 0

        while read_idx < n:
            if nums[read_idx] != 0:
                nums[write_idx] = nums[read_idx]
                write_idx += 1
            read_idx += 1
        
        while write_idx < n:
            nums[write_idx] = 0
            write_idx += 1
