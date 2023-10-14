from typing import List
from collections import defaultdict

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.dd = defaultdict(list)

    def insertRow(self, name: str, row: List[str]) -> None:
        row_id = 1 if not self.dd[name] else self.dd[name][-1][0] + 1
        row_content = [row_id, True] + row
        self.dd[name].append(row_content)
        
    def deleteRow(self, name: str, rowId: int) -> None:
        self.dd[name][rowId - 1][1] = False
        
    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        if not self.dd[name][rowId - 1][1]:
            return ""
        return self.dd[name][rowId - 1][columnId + 1]