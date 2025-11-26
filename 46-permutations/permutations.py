class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        seen = set()

        def dfs(i, returnValueParam, current):
            if len(current) == len(nums):
                returnValueParam.append(current[:])
                return 
            
            for ic in range(len(nums)):
                if ic not in seen:
                    current.append(nums[ic])
                    seen.add(ic)
                    dfs(i, returnValueParam, current)
                    current.pop()
                    seen.remove(ic)

            return 

        returnValue = []
        for i in range(len(nums)):
            seen.add(i)
            dfs(i, returnValue, [nums[i]])
            seen.remove(i)
        
        return returnValue

        