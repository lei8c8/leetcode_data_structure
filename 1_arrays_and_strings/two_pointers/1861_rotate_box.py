from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        for i in range(m):
            drop_place = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '*':
                    drop_place = j - 1
                if box[i][j] == '#':
                   box[i][j], box[i][drop_place] =  box[i][drop_place], box[i][j]
                   drop_place -= 1
        
        return list(zip(*box[::-1]))