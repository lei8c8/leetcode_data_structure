class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):

        def cap(x):
            curr, ans = 0, 0
            for num in nums:
                curr = curr + 1 if num <= x else 0
                ans += curr
            return ans

        return cap(right) - cap(left - 1)


if __name__ == '__main__':
    solution = Solution()
    data = [73,55,36,5,55,14,9,7,72,52]
    left, right = 32, 69
    result = solution.numSubarrayBoundedMax(data, left, right)
    print(result)