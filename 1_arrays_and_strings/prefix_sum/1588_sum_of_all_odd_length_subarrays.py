from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_sum = [arr[0]]
        ans = 0

        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + arr[i])

        for left in range(n):
            right = left
            while right < n:
                if left == 0:
                    ans += prefix_sum[right]
                else:
                    value = prefix_sum[right] - prefix_sum[left - 1]
                    ans += value
                right += 2

        return ans


        