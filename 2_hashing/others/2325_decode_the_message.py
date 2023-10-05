class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        lower_case_letters = [chr(ord('a') + i) for i in range(26)]
        mapping, i = {}, 0

        for v in key:
            if v == " " or v in mapping:
                continue
            mapping[v] = lower_case_letters[i]
            i += 1

        ans = list(message)

        for i in range(len(ans)):
            if ans[i] == " ":
                continue
            ans[i] = mapping[ans[i]]

        return ''.join(ans)
