"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # append result
        result=[]
        #use the depth first approcah
        def dfs(node):
            if not node:
                return 
            # as per the defination depth first search will go inside the child node 
            for child in node.children:
                dfs(child) # going from the inddepth
            result.append(node.val)
        # calling function
        dfs(root)
        return result
        
