class Solution:
    def next_permutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]

    def getMinSwaps(self, num, k):
        kth_permutation = list(num)
        num_list = list(num)

        for _ in range(k):
            self.next_permutation(kth_permutation)

        ans = 0
        n = len(num_list)
        for i in range(n):
            j = i
            while j < n and num_list[j] != kth_permutation[i]:
                j += 1
            ans += j - i
            num_list[i:j+1] = [num_list[j]] + num_list[i:j]
        return ans