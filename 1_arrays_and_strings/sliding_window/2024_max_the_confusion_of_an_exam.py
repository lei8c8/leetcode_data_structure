class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left, ans, curr = 0, 0, {}

        for right in range(len(answerKey)):
            curr[answerKey[right]] = curr.get(answerKey[right], 0) + 1
            while min(curr.get('T', 0), curr.get('F', 0)) > k:
                curr[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

