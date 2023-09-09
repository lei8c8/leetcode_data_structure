class Solution:
    def getModifiedArray(self, length, updates):
        ans = [0] * length

        for start, end, v in updates:
            ans[start] += v
            if end < length - 1:
                ans[end + 1] -= v

        for i in range(1, length):
            ans[i] += ans[i - 1]

        return ans
