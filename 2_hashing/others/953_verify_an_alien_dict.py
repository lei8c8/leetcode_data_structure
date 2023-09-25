class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        lowercase_letters = [chr(ord('a') + i) for i in range(26)]
        order_map = {v: i for i, v in enumerate(order)}
        expected = sorted(words, key = lambda x: ''.join([lowercase_letters[order_map[c]] for c in x]))
        return expected == words
    

if __name__ == '__main__':
    solution = Solution()
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    result1 = solution.isAlienSorted(words, order)
    print(f"result1 = {result1}")

    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    result2 = solution.isAlienSorted(words, order)
    print(f"result2 = {result2}")

    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    result3 = solution.isAlienSorted(words, order)
    print(f"result3 = {result3}")