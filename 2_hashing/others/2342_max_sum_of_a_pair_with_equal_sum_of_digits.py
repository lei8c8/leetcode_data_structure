from collections import defaultdict

class Solution:
    def maximumSum(self, nums: list[int]) -> int:

        def calculate_sum_of_digits(num):
            ans = 0
            while num:
                ans += num % 10
                num //= 10
            return ans
        
        digits_sum = defaultdict(int)
        result = -1
        
        for num in nums:
            s = calculate_sum_of_digits(num)
            if s in digits_sum:
                result = max(result, num + digits_sum[s])
            digits_sum[s] = max(digits_sum[s], num)
            
        return result
