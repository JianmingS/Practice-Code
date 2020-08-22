# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.init()

    def init(self):
        self.child_to_father = dict()
        self.leafs = []

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.init()
        self.scan_tree(root, 1)
        ret = 0

        for index, val in enumerate(self.leafs):
            for val2 in self.leafs[index + 1:]:
                val1 = val
                cnt = 0
                while val1 != val2 and cnt <= distance:
                    if val1 > val2:
                        val1 //= 2
                    else:
                        val2 //= 2
                    cnt += 1
                if cnt <= distance:
                    ret += 1

        return ret

    def scan_tree(self, root, val):
        root.val = val

        if root.left:
            left_val = val*2
            self.scan_tree(root.left, left_val)
            self.child_to_father[left_val] = val

        if root.right:
            right_val = val*2 + 1
            self.scan_tree(root.right,  right_val)
            self.child_to_father[right_val] = val

        if not root.left and not root.right:
            self.leafs.append(val)
