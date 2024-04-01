"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node
        q = deque()
        q.append(node)
        clones = {}
        clones[node.val] = Node(node.val, [])
        while q:
            curr = q.popleft()
            curr_node = clones[curr.val]
            for neighbor in curr.neighbors:

                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)

                curr_node.neighbors.append(clones[neighbor.val])

        return clones[node.val]
