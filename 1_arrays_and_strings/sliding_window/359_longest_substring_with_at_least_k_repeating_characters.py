import string

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans, total_unique = 0, len(set(s))

        for curr_unique in range(1, total_unique + 1):
            ct = {c: 0 for c in string.ascii_lowercase}
            start, end, unique_letters, at_least_k = 0, 0, 0, 0
            while end < len(s):
                if unique_letters <= curr_unique:
                    if ct[s[end]] == 0:
                        unique_letters += 1
                    ct[s[end]] += 1
                    if ct[s[end]] == k:
                        at_least_k += 1
                    end += 1
                else:
                    if ct[s[start]] == k:
                        at_least_k -= 1
                    ct[s[start]] -= 1
                    if ct[s[start]] == 0:
                        unique_letters -= 1
                    start += 1
                if unique_letters == curr_unique and unique_letters == at_least_k:
                    ans = max(ans, end - start)

        return ans


        
