class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        s1 = set()
        s2 = set()
        ans = [0] * len(A)

        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            ans[i] = len(s1.intersection(s2))

        return ans