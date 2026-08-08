# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        right, left = 0, 0
        if root.right != None:
            right = self.maxDepth(root.right)
        
        if root.left != None:
            left = self.maxDepth(root.left)

        return 1 + max(right, left)

        
     
            
        

        
        return 1
            



        