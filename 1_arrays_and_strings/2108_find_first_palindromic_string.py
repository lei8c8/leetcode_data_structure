from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def is_palindrome(s):
            if len(s) <= 1:
                return True
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word

        return ""

            