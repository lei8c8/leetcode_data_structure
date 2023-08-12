class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1, p2 = 0, 0
        n1, n2 = len(word), len(abbr)
        while p1 < n1 and p2 < n2:
            if abbr[p2].isalpha():
                if word[p1] != abbr[p2]:
                    return False
                p1 += 1
                p2 += 1
            else:
                if abbr[p2] == '0':
                    return False
                else:
                    num = int(abbr[p2])
                    while p2 + 1 < n2 and abbr[p2 + 1].isdigit():
                        num = 10 * num + int(abbr[p2 + 1])
                        p2 += 1
                    p2 += 1
                    p1 += num
        return p1 == n1 and p2 == n2
