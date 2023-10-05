class Solution:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        i = 1
        j = 1
        m = {1: 1}

        while True:
            i = (i + j * k) % n if (i + j * k) % n else 0
            m[i] = m.get(i, 0) + 1
            if m[i] > 1:
                break
            j += 1

        return [x for x in range(1, n + 1) if x not in m]
        