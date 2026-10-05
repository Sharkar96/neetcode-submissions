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
        if not node: return None
        dq = deque([node])

        m[node] = Node(node.val)
        
        while dq:
            current = dq.popleft()
            if current not in m:
                m[current] = Node(current.val)

            for neighbor in current.neighbors:
                if neighbor not in m:
                    dq.append(neighbor)
                    m[neighbor] = Node(neighbor.val)
                m[current].neighbors.append(m[neighbor])
                
                    

        return m[node]




        