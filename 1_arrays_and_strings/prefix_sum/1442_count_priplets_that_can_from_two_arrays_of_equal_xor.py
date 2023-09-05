class Solution:
    def countTriplets(self, arr):
        ans = 0
        for left in range(len(arr) - 1):
            curr_xor = arr[left]
            for right in range(left + 1, len(arr)):
                if arr[right] ^ curr_xor == 0:
                    ans += right - left
                curr_xor ^= arr[right]
        return ans