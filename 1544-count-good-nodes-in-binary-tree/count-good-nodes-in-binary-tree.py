# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal, goods):

            if not node:
                return goods

            if node.val >= maxVal:
                goods[0] += 1
                print(goods, node.val)

            
            dfs(node.left, max(node.val, maxVal), goods)
            dfs(node.right, max(node.val, maxVal), goods)

        goods = [0]
        dfs(root, float('-inf'), goods)
        return goods[0]