# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        ans = []

        queue = deque([root])

        while queue:
            curr_level_len = len(queue)
            for i in range(curr_level_len):
                curr_node = queue.popleft()
                if i == curr_level_len - 1:
                    ans.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        
        return ans