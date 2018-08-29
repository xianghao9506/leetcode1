class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = [i for i, v in enumerate(words) if v == word1] ### *****
        l2 = [i for i, v in enumerate(words) if v == word2] ### *****
        min = len(words)
        for x in l1:
            for y in l2:
                if abs(x - y) < min:
                    min = abs(x - y)

        return min

