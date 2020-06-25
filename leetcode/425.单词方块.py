class Solution:
    def __init__(self):
        self.words = None
        self.trie = None

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words

        # self.trie = {}
        # self.build_trie()

        self.prefix_hash_table = {}
        self.build_prefix_hash_table()

        results = []
        self.solve(0, [], results)
        return results

    def solve(self, step, word_ls, results):
        if step == len(self.words[0]):
            results.append(word_ls[:])
            return

        prefix = ''.join([w[step] for w in word_ls])
        for w in self.get_prefix_words(prefix):
            word_ls.append(w)
            self.solve(step + 1, word_ls, results)
            word_ls.pop()

    def get_prefix_words(self, prefix):
        if not prefix:
            return self.words

        # trie = self.trie
        # for ch in prefix:
        #     if ch not in trie:
        #         return []
        #     trie = trie[ch]

        # return [self.words[i] for i in trie['#']]

        return [self.words[i] for i in self.prefix_hash_table.get(prefix) or []]

    # def build_trie(self):
    #     for index, w in enumerate(self.words):
    #         trie = self.trie
    #         for ch in w:
    #             if ch not in trie:
    #                 trie[ch] = {}
    #                 trie[ch]['#'] = []
    #             trie = trie[ch]
    #             trie['#'].append(index)

    def build_prefix_hash_table(self):
        for index, w in enumerate(self.words):
            for prefix in (w[:i] for i in range(1, len(w))):
                self.prefix_hash_table.setdefault(prefix, []).append(index)
