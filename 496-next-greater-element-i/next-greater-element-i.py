class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)

        stack = []
        ngm = {}

        for num in nums2:

            while stack and num > stack[-1]:
                ngm[stack.pop()] = num
                result.append(num)
            stack.append(num)

        return [ngm[n] if n in ngm else -1 for n in nums1]
            



            
        