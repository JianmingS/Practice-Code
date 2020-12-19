"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        cur = Node(root.val)
        children = []

        for child in root.children:
            children.append(self.cloneTree(child))

        cur.children = children
        return cur