class Solution:
    def findMaxK(self, nums):
        pair_dict = {}
        for num in nums:
            if abs(num) not in pair_dict:
                pair_dict[abs(num)] = []
                pair_dict[abs(num)].append(num)
            else:
                if num not in pair_dict[abs(num)]:
                    pair_dict[abs(num)].append(num)
        for x in sorted(pair_dict, key=lambda x: -x):
            if len(pair_dict[x]) == 2:
                return x
        return -1
