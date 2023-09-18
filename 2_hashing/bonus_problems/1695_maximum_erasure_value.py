class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()
        win_left = 0
        ans, curr = 0, 0
        for win_right in range(len(nums)):
            curr += nums[win_right]
            while nums[win_right] in seen:
                seen.remove(nums[win_left])
                curr -= nums[win_left]
                win_left += 1
            seen.add(nums[win_right])
            ans = max(ans, curr)
        return ans
        
        