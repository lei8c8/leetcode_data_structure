# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root, k):
        values = []

        def dfs(root, values):
            if not root:
                return None
            dfs(root.left, values)
            values.append(root.val)
            dfs(root.right, values)

        dfs(root, values)
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] + values[right] == k:
                return True
            elif values[left] + values[right] < k:
                left += 1
            else:
                right -= 1
        return False