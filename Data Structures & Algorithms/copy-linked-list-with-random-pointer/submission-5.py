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
        new_node = defaultdict(lambda: Node(0))
        new_node[None] = None

        cur = head
        while cur:
            new_node[cur].val = cur.val
            new_node[cur].next = new_node[cur.next]
            new_node[cur].random = new_node[cur.random]
            cur = cur.next
        
        return new_node[head]
