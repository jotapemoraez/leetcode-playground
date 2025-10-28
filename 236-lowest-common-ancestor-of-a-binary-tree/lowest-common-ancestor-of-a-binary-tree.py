# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.founds = 0
        self.value = None
        self.candidate = None
        
        def dfs(node):
            
            if not node:
                return None

            if (node.val == p.val or node.val == q.val):
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            elif left and right is None:
                return left
            elif right and left is None:
                return right
            else:
                return None
                 

        
        

        return dfs(root)

            
        