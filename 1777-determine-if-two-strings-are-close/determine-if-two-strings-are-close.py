class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        
        count1 = sorted(list(freq1.values()))
        count2 = sorted(list(freq2.values()))

        return count1 == count2