from collections import defaultdict

class Solution:
    def maxSum(self, nums: list[int]) -> int:
        dd = defaultdict(list)
        ans = -1

        for num in nums:
            max_digit = max(str(num))
            dd[max_digit].append(num)

        for key in dd:
            if len(dd[key]) >= 2:
                dd[key].sort(reverse=True)
                ans = max(ans, dd[key][0] + dd[key][1])

        return ans