class Solution:
    def pancakeSort(self, arr):
        start = len(arr)
        ans = []
        while start > 0:
            idx = arr.index(start)
            position = start - 1
            if idx != position:
                if idx != 0:
                    ans.append(idx + 1)
                    arr[:idx + 1] = arr[:idx + 1][::-1]
                ans.append(position + 1)
                arr[:position + 1] = arr[:position + 1][::-1]
            start -= 1

        return ans