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
        nextLevel = deque()

        ret = []

        while currentLevel or nextLevel:

            level = []
            while currentLevel:
                node = currentLevel.popleft()
                level.append(node.val)

                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            #finito il livello current
            if level:
                ret.append(level)

            level = []
            while nextLevel:
                node = nextLevel.popleft()
                level.append(node.val)

                if node.left:
                    currentLevel.append(node.left)
                if node.right:
                    currentLevel.append(node.right)
            #finito il livello next
            if level:
                ret.append(level)
        
        return ret

                


            



        