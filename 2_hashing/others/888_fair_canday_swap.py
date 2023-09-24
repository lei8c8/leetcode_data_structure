class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        alice_total, bob_total = sum(aliceSizes), sum(bobSizes)
        bob_set = set(bobSizes)

        for x in aliceSizes:
            if ((bob_total - alice_total  + 2 * x) % 2 == 0 and 
                (bob_total - alice_total  + 2 * x) // 2 in bob_set):
                return [x, (bob_total - alice_total  + 2 * x) // 2]
