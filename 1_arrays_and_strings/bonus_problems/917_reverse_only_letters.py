class Solution:
    def reverseOnlyLetters(self, s):
        # 32 ms (two pointers)
        left, right = 0, len(s) - 1
        ans = list(s)
        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
            if left != right:
                ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ''.join(ans)


class Solution2:
    def reverseOnlyLetters(self, s):
        # 41 ms (stack)
        stack = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(stack.pop())
            else:
                ans.append(c)
        return ''.join(ans)
    

class Solution3:
    def reverseOnlyLetters(self, s):
        # 45 ms (reversed pointer)
        ans = []
        right = len(s) - 1
        for c in s:
            if c.isalpha():
                while not s[right].isalpha():
                    right -= 1
                ans.append(s[right])
                right -= 1
            else:
                ans.append(c)
        return ''.join(ans)