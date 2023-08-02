from typing import List

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(encoded1), len(encoded2)
        idx1, idx2, encoded_product = 0, 0 , []

        while idx1 < n1 and idx2 < n2:
            v1, freq1 = encoded1[idx1]
            v2, freq2 = encoded2[idx2]
            proudct = v1 * v2
            min_freq = min(freq1, freq2)
            encoded1[idx1][1] -= min_freq
            encoded2[idx2][1] -= min_freq

            if encoded1[idx1][1] == 0:
                idx1 += 1
            if encoded2[idx2][1] == 0:
                idx2 += 1

            if not encoded_product or encoded_product[-1][0] != proudct:
                encoded_product.append([proudct, min_freq])
            else:
                encoded_product[-1][1] += min_freq

        return encoded_product



        
