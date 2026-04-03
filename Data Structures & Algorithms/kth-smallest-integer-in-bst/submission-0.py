# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None

        ans = []
        self.inOrder(root, ans)
        return ans[k-1]

    def inOrder(self, node, ans):
        if not node:
            return
        self.inOrder(node.left, ans)
        ans.append(node.val)
        self.inOrder(node.right, ans)