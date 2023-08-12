from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right, count = [], [], 0

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                count += 1
                
        for _ in range(count):
            left.append(pivot)
        
        return left + right