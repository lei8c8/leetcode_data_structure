class Solution:
    def maxVowels(self, s, k):
        curr_vowels, window_start = 0, 0
        vowels = set("aeiou")

        for i in range(k):
            if s[i] in vowels:
                curr_vowels += 1

        ans = curr_vowels

        for window_end in range(k, len(s)):
            if s[window_end] in vowels:
                curr_vowels += 1
            if s[window_start] in vowels:
                curr_vowels -= 1
            ans = max(ans, curr_vowels)
            window_start += 1

        return ans


