# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = []
        next_queue = []

        queue.append(root)

        while queue:
            next_queue = []

            for node in queue:
                if not node:
                    break

                temp_node = node.left
                node.left = node.right
                node.right = temp_node

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            queue = next_queue
            
        return root
        