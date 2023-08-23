from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        if len(arr) < k:
            return ans
        
        curr = 0
        compare_to = k * threshold

        for i in range(k):
            curr += arr[i]

        if curr >= compare_to:
            ans = 1

        for i in range(k, len(arr)):
            curr += arr[i] - arr[i - k]
            if curr >= compare_to:
                ans += 1
        return ans