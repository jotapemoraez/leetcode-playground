# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:      
        self.biggest = 0
        def dfs(node):
            if not node:
                return 0

            if not node.left and not node.right:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            self.biggest = max(left+right, self.biggest)

            return 1 + max(left, right)

        dfs(root)

        return self.biggest
        