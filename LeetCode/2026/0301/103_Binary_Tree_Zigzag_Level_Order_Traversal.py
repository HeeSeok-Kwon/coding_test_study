# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] # 결과 담을 변수
        left_to_right = True # 결과 담을 방향 변수
        
        # root에 아무것도 없을 때
        if not root:
            return result

        queue = []
        next_queue = []
        level_vals = []

        queue.append(root)

        while queue:
            next_queue = []
            level_vals = []

            for node in queue:

                level_vals.append(node.val)

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            queue = next_queue
            
            if left_to_right:
                left_to_right = not left_to_right
                pass
            else:
                left_to_right = not left_to_right
                level_vals.reverse()

            result.append(level_vals)

        return result
