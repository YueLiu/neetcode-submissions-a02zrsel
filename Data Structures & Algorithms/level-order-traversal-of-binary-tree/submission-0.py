# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])

        while queue:
            curr_level_nodes = []
            curr_level_len = len(queue)
            for _ in range(curr_level_len):
                curr_node = queue.popleft()
                curr_level_nodes.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            ans.append(curr_level_nodes)
        
        return ans
