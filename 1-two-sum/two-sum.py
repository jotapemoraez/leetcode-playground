class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapKey = {}

        for i in range(len(nums)):
            value = nums[i]
            complement = target - value
           
            if complement in mapKey:
                return [mapKey[complement], i]
            else:
                mapKey[nums[i]] = i
        
        return [-1,-1]
        