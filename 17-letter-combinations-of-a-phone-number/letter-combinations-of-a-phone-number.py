class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")

        result = []
        path = []
        def backtrack(i):
            if i == len(digits):
                result.append("".join(path))
                return 

            digit = int(digits[i])

            for ch in letters[digit]:
                path.append(ch)
                backtrack(i+1)
                path.pop()

       
        backtrack(0)
        return result