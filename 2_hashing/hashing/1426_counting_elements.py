class Solution:
    def countElements(self, arr):
        ct, ans = {}, 0
        
        for x in arr:
            ct[x] = ct.get(x, 0) + 1

        for key in ct:
            if key + 1 in ct:
                ans += ct[key]
        
        return ans
