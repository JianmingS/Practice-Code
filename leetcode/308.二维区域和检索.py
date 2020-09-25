class TreeNode(object):
    def __init__(self, left_row, left_col, right_row, right_col, children, total):
        self.left_row = left_row
        self.left_col = left_col
        self.right_row = right_row
        self.right_col = right_col
        self.children = children
        self.total = total


class SegmentTree():

    def __init__(self, matrix):
        self.matrix = matrix
        if self.matrix and len(self.matrix) > 0:
            self.root = self.build(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
        else:
            self.root = None

    def build(self, left_row, left_col, right_row, right_col):
        if left_row > right_row or left_col > right_col:
            return None

        if left_row == right_row and left_col == right_col:
            return TreeNode(left_row, left_col, right_row, right_col, [], self.matrix[left_row][right_col])

        mid_row = (left_row + right_row) >> 1
        mid_col = (left_col + right_col) >> 1

        children = [
            self.build(left_row, left_col, mid_row, mid_col),
            self.build(left_row, mid_col + 1, mid_row, right_col),
            self.build(mid_row + 1, left_col, right_row, mid_col),
            self.build(mid_row + 1, mid_col + 1, right_row, right_col)
        ]

        total = 0
        for child in children:
            total += child and child.total or 0
        return TreeNode(left_row, left_col, right_row, right_col, children, total)

    def update(self, row, col, val):
        def __update(root, row, col, val):
            if not (root and root.left_row <= row <= root.right_row and root.left_col <= col <= root.right_col):
                return

            if root.left_row == row and root.left_col == col and root.right_row == row and root.right_col == col:
                root.total = val
                self.matrix[row][col] = val
                return

            for child in root.children:
                __update(child, row, col, val)

            total = 0
            for child in root.children:
                total += child and child.total or 0

            root.total = total

        __update(self.root, row, col, val)

    def query(self, left_row, left_col, right_row, right_col):
        def __query(root, left_row, left_col, right_row, right_col):
            if not (root
                    and root.left_row <= left_row <= root.right_row and root.left_col <= left_col <= root.right_col
                    and root.left_row <= right_row <= root.right_row and root.left_col <= right_col <= root.right_col
                    ):
                return 0

            if root.left_row == left_row and root.left_col == left_col and root.right_row == right_row and root.right_col == right_col:
                return root.total

            mid_row = (root.left_row + root.right_row) >> 1
            mid_col = (root.left_col + root.right_col) >> 1

            ret = 0
            ret += __query(
                root.children[0],
                left_row, left_col,
                min(mid_row, right_row), min(mid_col, right_col)
            )
            ret += __query(
                root.children[1],
                left_row, max(mid_col + 1, left_col),
                min(mid_row, right_row), right_col
            )
            ret += __query(
                root.children[2],
                max(mid_row + 1, left_row), left_col,
                right_row, min(right_col, mid_col)
            )
            ret += __query(
                root.children[3],
                max(mid_row + 1, left_row), max(mid_col + 1, left_col),
                right_row, right_col
            )

            return ret

        return __query(self.root, left_row, left_col, right_row, right_col)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.segment_tree = SegmentTree(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        self.segment_tree.update(row, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.segment_tree.query(row1, col1, row2, col2)
