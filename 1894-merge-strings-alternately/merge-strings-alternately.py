class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        arr = []
        for ch1, ch2 in zip(word1,word2):
            arr.extend([ch1,ch2])

        arr.extend(word1[n:])
        arr.extend(word2[n:])

        return "".join(arr)
