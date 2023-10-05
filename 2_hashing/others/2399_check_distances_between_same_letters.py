class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        first_occurence = {}
        for i, v in enumerate(s):
            if v not in first_occurence:
                first_occurence[v] = i
            else:
                d = i - first_occurence[v] - 1
                idx = ord(v) - ord('a')
                if distance[idx] != d:
                    return False
        return True
