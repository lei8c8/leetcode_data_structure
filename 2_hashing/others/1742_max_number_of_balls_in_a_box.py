class Solution:
    def countBalls(self, low: int, high: int) -> int:

        def get_box_id(x):
            ans = 0
            while x > 0:
                ans += x % 10
                x //= 10
            return ans

        ct = {}
        for x in range(low, high + 1):
            box_id = get_box_id(x)
            ct[box_id] = ct.get(box_id, 0) + 1
        return max(ct.values())