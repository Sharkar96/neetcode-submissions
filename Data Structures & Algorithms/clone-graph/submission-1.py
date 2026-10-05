"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        m = {}
        
        def dfs(nodee):
            if not nodee: return None
            if nodee in m: return m[nodee]

            m[nodee] = Node(nodee.val)

            for n in nodee.neighbors:
                m[nodee].neighbors.append(dfs(n))
            return m[nodee]

        return dfs(node) if node else None
            



        