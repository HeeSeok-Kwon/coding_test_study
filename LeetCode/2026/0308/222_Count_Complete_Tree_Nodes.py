# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        result = 0 # 결과 담을 변수
        
        # root에 아무것도 없을 때
        if not root:
            return result

        queue = []
        next_queue = []

        queue.append(root)

        while queue:
            next_queue = []

            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

                result += 1

            queue = next_queue
            
        return result
        