class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        if nums[0] >= 0:
            return [n*n for n in nums]
        ind = 0
        while ind < len(nums) and nums[ind] < 0:
            ind += 1

        left = ind - 1
        right = ind
        res = []
        while left >= 0 and right < len(nums):
            pLeft = pow(nums[left],2)
            pRight = pow(nums[right],2)
            
            if pLeft < pRight:
                res.append(pLeft)
                left -= 1
            else:
                res.append(pRight)
                right += 1
        
        while left >= 0:
            res.append(pow(nums[left],2))
            left -= 1

        while right < len(nums):
            res.append(pow(nums[right],2))
            right += 1
        
        return res