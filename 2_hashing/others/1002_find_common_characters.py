from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        ans = []
        ct = [Counter(word) for word in words] 

        for c in set(words[0]):
            repeated = min(ct[i][c] for i in range(len(ct)))
            for _ in range(repeated):
                ans.append(c)

        return ans
    

if __name__ == "__main__":
    solution = Solution()

    words = ["bella","label","roller"]
    result = solution.commonChars(words)
    print(result)

    words = ["cool","lock","cook"]
    result = solution.commonChars(words)
    print(result)