from collections import defaultdict

class Solution:
    def __init__(self):
        self.adjacency_list = None
        self.node_label_cnt = None
        self.labels = None

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.adjacency_list = self.get_adjacency_list(edges)
        self.node_label_cnt = [[0]*26 for _ in range(len(labels))]
        self.labels = labels
        self.dfs(0, -1)
        return [self.node_label_cnt[i][ord(labels[i]) - ord('a')] for i in range(len(labels))]

    def dfs(self, node, father):
        self.node_label_cnt[node][ord(self.labels[node]) - ord('a')] = 1
        for child in self.adjacency_list[node]:
            if child == father:
                continue
            self.dfs(child, node)
            for i in range(26):
                self.node_label_cnt[node][i] += self.node_label_cnt[child][i]

    def get_adjacency_list(self, edges):
        ret = defaultdict(list)
        for begin, end in edges:
            ret[begin].append(end)
            ret[end].append(begin)
        return ret