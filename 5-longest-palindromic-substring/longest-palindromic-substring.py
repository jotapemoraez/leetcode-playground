class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        

        i = 0
        l = 0
        r = 0
        biggest = ''

        for i in range(len(s)):
            l = r = i
            current = ''
            while l >=0 and r < len(s) and s[l] == s[r]:
                current = s[l:r+1]
                l -= 1
                r += 1
            
            if len(current) > len(biggest):
                biggest = current

            l = i
            r = i+1
            current = ''
            while l >=0 and r < len(s) and s[l] == s[r]:
                current = s[l:r+1]
                l -= 1
                r += 1
            
            if len(current) > len(biggest):
                biggest = current

        return biggest
            
            


            


            








        