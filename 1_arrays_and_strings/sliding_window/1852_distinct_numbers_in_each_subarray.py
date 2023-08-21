class Solution:
    def distinctNumbers(self, nums, k):
        count_map = {}
        for i in range(k):
            count_map[nums[i]] = count_map.get(nums[i], 0) + 1

        ans = [len(count_map)]
        for i in range(k, len(nums)):
            count_map[nums[i]] = count_map.get(nums[i], 0) + 1
            count_map[nums[i - k]] -= 1
            if count_map[nums[i - k]] == 0:
                count_map.pop(nums[i - k])
            ans.append(len(count_map))
        return ans
