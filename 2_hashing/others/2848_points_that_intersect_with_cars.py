class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        s = set()

        for num in nums:
            start = num[0]
            end = num[1]
            for i in range(start, end + 1):
                s.add(i)

        return len(s)