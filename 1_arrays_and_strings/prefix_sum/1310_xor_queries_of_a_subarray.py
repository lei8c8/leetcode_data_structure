from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [arr[0]]

        for i in range(1, len(arr)):
            prefix_xor.append(prefix_xor[-1] ^ arr[i])

        ans = []
        for start, end in queries:
            if start == 0:
                ans.append(prefix_xor[end])
            else:
                ans.append(prefix_xor[end] ^ prefix_xor[start - 1])

        return ans