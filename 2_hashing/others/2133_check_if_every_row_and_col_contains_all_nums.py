class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        row_map = {i: set() for i in range(n)}
        col_map = {i: set() for i in range(n)}

        for row in range(n):
            for col in range(n):
                value = matrix[row][col]
                if value in row_map[row] or value in col_map[col]:
                    return False
                row_map[row].add(value)
                col_map[col].add(value)

        return True