# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        maxZig = [0]

        def dfs(node, depth=0, fromSide=0):

            if not node:
                return
            
            if fromSide == 1:
                if node.left:
                    maxZig[0] = max(maxZig[0], depth+1)
                    dfs(node.left, depth+1, 2)
                if node.right:
                    dfs(node.right, 1, 1)
            else:
                if node.right:
                    maxZig[0] = max(maxZig[0], depth+1)
                    dfs(node.right, depth+1, 1)
                if node.left:
                    dfs(node.left, 1, 2)
        dfs(root)

        return maxZig[0]
                    

        