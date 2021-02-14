from collections import defaultdict

class Solution:
    # 双指针
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ret = float('INF')
        word1_last_pos = None
        word2_last_pos = None

        for i, word in enumerate(words):
            if word == word1:
                word1_last_pos = i
                if word2_last_pos:
                    ret = min(ret, word1_last_pos - word2_last_pos)
            
            if word == word2:
                word2_last_pos = i
                if word1_last_pos:
                    ret = min(ret, word2_last_pos - word1_last_pos)
        
        return ret

    # me
    def findClosest1(self, words: List[str], word1: str, word2: str) -> int:
        word_to_pos_list = defaultdict(list)
        for i, word in enumerate(words):
            word_to_pos_list[word].append(i)
        return self.get_min_distance(word_to_pos_list[word1], word_to_pos_list[word2])
    
    def get_min_distance(self, ls1, ls2):
        ret = float('INF')
        for pos1 in ls1:
            tmp = float('INF')
            for pos2 in ls2:
                dis = abs(pos2 - pos1)
                if dis >= tmp:
                    break
                tmp = dis
            ret = min(tmp, ret)
        return ret

