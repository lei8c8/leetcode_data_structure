class Solution:
    def reverseWords(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse_list(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        def reverse_word_only(l):
            left, right = 0, 0
            while left < len(l):
                while right < len(l) and l[right] != " ":
                    right += 1
                reverse_list(l, left, right - 1)
                left = right + 1
                right = left

        reverse_list(s, 0, len(s) - 1)
        reverse_word_only(s)
        
