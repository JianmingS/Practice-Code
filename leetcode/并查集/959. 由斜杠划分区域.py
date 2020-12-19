class Dsu:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.cnt = n

    def find(self, x):
        if self.par[x] == x:
            return x
        return self.find(self.par[x])

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.par[x] != self.par[y]:
                self.rank[y] += 1

        self.cnt -= 1


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        length = len(grid)
        dsu = Dsu(4*length*length)

        for row in range(length):
            for col in range(length):
                node = (row * length + col) * 4

                if grid[row][col] != '\\':
                    dsu.unite(node + 0, node +3)
                    dsu.unite(node + 1, node + 2)

                if grid[row][col] != '/':
                    dsu.unite(node + 0, node + 1)
                    dsu.unite(node + 2, node + 3)
                
                if row < length - 1:
                    dsu.unite(node + 2, node + (length * 4) + 0)

                if col < length - 1:
                    dsu.unite(node + 1, node + 4 + 3)

        return dsu.cnt
