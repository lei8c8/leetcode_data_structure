class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        invald_count = 0
        arr2.sort()
        for x in arr1:
            left, right = 0, len(arr2) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if abs(x - arr2[mid]) <= d:
                    invald_count += 1
                    break
                elif arr2[mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1
        return len(arr1) - invald_count