# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        currentLevel = deque([root])

        ret = []

        while currentLevel:

            level = []
            levelElNum = len(currentLevel)
            while levelElNum > 0:
                node = currentLevel.popleft()
                levelElNum -= 1
                level.append(node.val)

                if node.left:
                    currentLevel.append(node.left)
                if node.right:
                    currentLevel.append(node.right)
            #finito il livello
            if level:
                ret.append(level)

        
        return ret
