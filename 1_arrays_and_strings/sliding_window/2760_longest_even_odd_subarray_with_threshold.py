class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        n, ans, visited = len(nums), 0, set()
        for i in range(n):
            if i in visited or nums[i] > threshold or nums[i] % 2 == 1:
                continue
            left = right = i
            while right + 1 < n and nums[right + 1] <= threshold and ((nums[right] % 2) ^ (nums[right + 1] % 2) == 1):
                right += 1
                visited.add(right)
            ans = max(ans, right - left + 1)
        return ans
