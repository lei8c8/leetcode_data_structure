class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_counts = 0

        for i in range(k):
            if blocks[i] == "W":
                white_counts += 1

        ans = white_counts
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                white_counts += 1
            if blocks[i - k] == "W":
                white_counts -= 1
            ans = min(ans, white_counts)

        return ans