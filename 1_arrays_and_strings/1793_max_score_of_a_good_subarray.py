
class Solution:
    def maximumScore(self, nums, k):
        left, right, ans, curr_min = k, k, nums[k], nums[k]

        while left >= 0 or right < len(nums):
            if left == 0 and right == len(nums) - 1:
                break 
            elif right == len(nums) - 1:
                left -= 1
            elif left == 0:
                right += 1
            elif nums[right + 1] > nums[left - 1]:
                right += 1
            else:
                left -= 1
            curr_min = min(curr_min, nums[left], nums[right])
            ans = max(ans, curr_min * (right - left + 1))
            
        return ans