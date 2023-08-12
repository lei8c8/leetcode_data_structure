class Solution:
    def diStringMatch(self, s):
        smallest, largest, ans = 0, len(s), []
        for c in s:
            if c == 'I':
                ans.append(smallest)
                smallest += 1
            else:
                ans.append(largest)
                largest -= 1
        ans.append(largest)
        return ans