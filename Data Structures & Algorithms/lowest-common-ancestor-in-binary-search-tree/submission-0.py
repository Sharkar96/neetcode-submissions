# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #if current less than p and q we go to the right subtree
        #if current more than p and q we go to the left subtree
        def dfs(current):
            if current == p or current == q:
                return current

            if current.val < p.val and current.val < q.val:
                return dfs(current.right) 
            if current.val > p.val and current.val > q.val:
                return dfs(current.left) 
            if p.val < current.val and current.val < q.val:
                return current
            if q.val < current.val and current.val < p.val:
                return current
        
        return dfs(root)
