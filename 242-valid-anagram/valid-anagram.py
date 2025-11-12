class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqS = {}
        for ch in s:
            freqS[ch] = freqS.setdefault(ch, 0) + 1

        freqT = {}
        for ch in t:
            freqT[ch] = freqT.setdefault(ch, 0) + 1

        for a in freqT:
            if a not in freqS or freqT[a] != freqS[a]:
                return False
            
        
        return True

        