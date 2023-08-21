class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        curr_calories, performance = sum(calories[:k]), 0
        if curr_calories < lower:
            performance = -1
        elif curr_calories > upper:
            performance = 1

        for i in range(k, len(calories)):
            curr_calories += calories[i] - calories[i - k]
            if curr_calories < lower:
                performance -= 1
            elif curr_calories > upper:
                performance += 1
        return performance

        