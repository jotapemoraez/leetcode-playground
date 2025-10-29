# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque([root])

        maxVal, maxLevel, level = float('-inf'), 0, 0
        while q:

            currVal = 0
            size = len(q)
            level += 1
            for i in range(0, size):

                node = q.popleft()

                currVal += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if currVal > maxVal:
                maxVal = currVal
                maxLevel = level
        

        return maxLevel
            




        