class Solution:
    def reversePrefix(self, word, ch):
        # 47 ms (two pointer)
        first_occurrence = -1
        word_list = list(word)
        
        for i, v in enumerate(word_list):
            if v == ch:
                first_occurrence = i
                break

        if first_occurrence <= 0:
            return word
        
        left, right = 0, first_occurrence
        while left < right:
            word_list[left], word_list[right] = word_list[right], word_list[left]
            left += 1
            right -= 1
            
        return ''.join(word_list)


class Solution2:
    def reversePrefix(self, word, ch):
        # 47 ms (two pointer)
        try:
            first = word.index(ch)
        except ValueError:
            first = -1
        return word[:first + 1][::-1] + word[first + 1:] if first > 0 else word