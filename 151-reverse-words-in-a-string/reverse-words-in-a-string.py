class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        arrClean = [word for word in arr if word]
        reverse = arrClean[::-1]

        return " ".join(reverse)
        