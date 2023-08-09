class Solution:
    def intervalIntersection(self, firstList, secondList):
        ans = []
        first_p, second_p = 0, 0
        while first_p < len(firstList) and second_p < len(secondList):
            left = max(firstList[first_p][0], secondList[second_p][0])
            right = min(firstList[first_p][1], secondList[second_p][1])
            if left <= right:
                ans.append([left, right])
            if firstList[first_p][1] < secondList[second_p][1]:
                first_p += 1
            else:
                second_p += 1
        return ans