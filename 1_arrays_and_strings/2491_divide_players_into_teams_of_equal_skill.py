from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        teams, total = len(skill) // 2, sum(skill)
        if total % teams != 0:
            return -1

        skill.sort()
        expected_team_value, total_chemistry = total // teams, 0
        left, right = 0, len(skill) - 1
        
        while left < right:
            if skill[left] + skill[right] != expected_team_value:
                return -1
            total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1

        return total_chemistry