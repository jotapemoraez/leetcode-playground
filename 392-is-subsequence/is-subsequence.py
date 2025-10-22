class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if len(t) < len(s):
            return False

        left = 0

        for rightCh in t:

            if rightCh == s[left]:
                left += 1
                if left == len(s):
                    return True
            
            
        
        return False



        