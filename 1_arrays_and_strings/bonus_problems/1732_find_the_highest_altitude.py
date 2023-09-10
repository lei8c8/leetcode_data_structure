class Solution:
    def largestAltitude(self, gain):
        ans, prev = 0, 0
        for g in gain:
            curr = prev + g
            ans = max(ans, curr)
            prev = curr
        return ans