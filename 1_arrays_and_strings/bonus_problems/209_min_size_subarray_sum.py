class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        ans, left, curr = n + 1, 0, 0
        
        for right in range(n):
            curr += nums[right]

            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1

        return ans if ans < n + 1 else 0

