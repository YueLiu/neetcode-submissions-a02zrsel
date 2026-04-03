# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validSubtree(root, float('-inf'), float('inf'))


    def validSubtree(self, node, lower_bound, upper_bound):
        if not node:
            return True
        if not lower_bound < node.val < upper_bound:
            return False
        lower_bound_right = node.val
        upper_bound_left = node.val
        return self.validSubtree(node.left, lower_bound, node.val) and self.validSubtree(node.right, node.val, upper_bound)
