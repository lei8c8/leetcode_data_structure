class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        x, y, seen = 0, 0, {(0, 0)}
        for d in path:
            x, y = x + direction[d][0], y + direction[d][1]
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False