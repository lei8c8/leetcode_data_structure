from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        distances = [10001] * n
        
        last_left_seen = -1
        for i in range(n):
            if s[i] == c:
                distances[i] = 0
                last_left_seen = i
            elif last_left_seen >= 0:
                distances[i] = i - last_left_seen

        last_right_seen = n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_right_seen = i
            elif last_right_seen != n:
                distances[i] = min(distances[i], last_right_seen - i)

        return distances
            