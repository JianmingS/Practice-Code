class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_to_val = dict([
            (i, val) for i, val in enumerate(nums) if val
        ])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ret = 0
        for index, val in self.index_to_val.items():
            ret += val * vec.index_to_val.get(index, 0)
        return ret
