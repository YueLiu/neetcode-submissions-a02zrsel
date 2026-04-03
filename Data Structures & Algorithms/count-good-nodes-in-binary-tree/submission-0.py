# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.dfs(root, root.val)

    def dfs(self, node, maxSeen):
        if not node:
            return 0
        ans = 1 if node.val >= maxSeen else 0

        maxSeen = max(node.val, maxSeen)

        ans += self.dfs(node.left, maxSeen)
        ans += self.dfs(node.right, maxSeen)

        return ans