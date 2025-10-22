class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        ni,nj = float('+inf'),float('+inf')
        
        for num in nums:
            if num <= ni:
                ni = num
            elif num < nj:
                nj = num
            elif num > nj:
                return True
            
            
            
        return False
        

        