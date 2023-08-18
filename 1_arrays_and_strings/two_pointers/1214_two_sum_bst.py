from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_dfs(self, root, list):
        if not root:
            return 
        self.inorder_dfs(root.left, list)
        list.append(root.val)
        self.inorder_dfs(root.right, list)

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        list1, list2 = [], []
        self.inorder_dfs(root1, list1)
        self.inorder_dfs(root2, list2)
        left = 0
        right = len(list2) - 1
        while left < len(list1) and right >= 0:
            if list1[left] + list2[right] == target:
                return True
            elif list1[left] + list2[right] < target:
                left += 1
            else:
                right -= 1
        return False
