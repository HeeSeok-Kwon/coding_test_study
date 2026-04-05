"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        clone = Node(head.val)
        visited = dict()
        visited[head] = clone

        queue = [head]

        while queue:
            current = queue.pop()

            if current.next and current.next not in visited:
                visited[current.next] = Node(current.next.val)
                queue.append(current.next)

            if current.random and current.random not in visited:
                visited[current.random] = Node(current.random.val)
                queue.append(current.random)

            visited[current].next = visited.get(current.next)
            visited[current].random = visited.get(current.random)

        return visited[head]
        
        