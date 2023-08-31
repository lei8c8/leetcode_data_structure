class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        def max_sum(first, second):
            ans, left_max = 0, 0
            for i in range(first, n - second + 1):
                left_max = max(left_max, prefix_sum[i] - prefix_sum[i - first])
                ans = max(ans, prefix_sum[i + second] - prefix_sum[i] + left_max)
            return ans
        
        return max(max_sum(firstLen, secondLen), max_sum(secondLen, firstLen))
                