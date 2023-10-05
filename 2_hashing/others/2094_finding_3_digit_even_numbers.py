from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        ct = Counter(digits)

        def check_if_valid(num):
            cloned_ct = ct.copy()
            for d in str(num):
                cloned_ct[int(d)] -= 1
            return all(n >= 0 for n in cloned_ct.values())

        ans = []
        for num in range(100, 1000):
            if num % 2 == 0 and check_if_valid(num):
                ans.append(num)
        return ans
            
        