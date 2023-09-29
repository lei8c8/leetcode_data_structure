from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:

        def calculate_digits_sum(x):
            ans = 0 
            while x > 0:
                ans += x % 10
                x //= 10
            return ans

        largest_group_count = 0
        ct = defaultdict(int)
        
        for x in range(1, n + 1):
            digits_sum = calculate_digits_sum(x)
            ct[digits_sum] += 1
            largest_group_count = max(largest_group_count, ct[digits_sum])

        result = 0
        for key in ct:
            if ct[key] == largest_group_count:
                result += 1


from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        def calculate_digits_sum(x):
            return sum(int(d) for d in str(x))

        ct = defaultdict(int)
        for x in range(1, n + 1):
            digits_sum = calculate_digits_sum(x)
            ct[digits_sum] += 1
        return sum(1 for key in ct if ct[key] == max(ct.values()))