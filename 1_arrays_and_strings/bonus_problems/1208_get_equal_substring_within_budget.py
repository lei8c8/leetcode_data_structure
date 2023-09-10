class Solution:
    def equalSubstring(self, s, t, max_cost):
        window_start, curr_cost, ans = 0, 0, 0

        for window_end in range(len(s)):
            curr_cost += abs(ord(s[window_end]) - ord(t[window_end]))

            while curr_cost > max_cost:
                curr_cost -= abs(ord(s[window_start]) - ord(t[window_start]))
                window_start += 1

            ans = max(ans, window_end - window_start + 1)

        return ans
    

class Solution2:
    def equalSubstring(self, s, t, max_cost):
        abs_delta = [abs(ord(x) - ord(y)) for x, y in zip(s, t)]
        left = cost = ans = 0
        for right in range(len(s)):
            cost += abs_delta[right]
            while cost > max_cost:
                cost -= abs_delta[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans