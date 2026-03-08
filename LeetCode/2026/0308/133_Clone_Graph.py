"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node
        
        clone = Node(node.val)
        visited = dict()
        visited[node] = clone
        
        queue = [node]

        while queue:
            current = queue.pop() # 피드백: popleft 사용을 권고 -> 내가 의도한 순서대로 디버깅이 가능

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    clone = Node(neighbor.val) # 복사
                    visited[neighbor] = clone
                    queue.append(neighbor)

                visited[current].neighbors.append(visited[neighbor]) # 그래프 연결

        return visited[node]

        
        